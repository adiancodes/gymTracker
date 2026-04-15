from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import timezone
from .models import Workout, DailyHydration

@ensure_csrf_cookie
def dashboard_view(request):
    today = timezone.localtime().date()
    
    # Handle simple form submission for new exercise
    if request.method == 'POST':
        exercise_type = request.POST.get('exercise_type')
        sets = request.POST.get('sets')
        reps = request.POST.get('reps')
        if exercise_type and sets and reps:
            Workout.objects.create(
                exercise_type=exercise_type,
                sets=int(sets),
                reps=int(reps)
            )
            return redirect('dashboard')
            
    workouts = Workout.objects.filter(date=today)
    hydration, created = DailyHydration.objects.get_or_create(date=today)
    
    context = {
        'workouts': workouts,
        'hydration': hydration,
        'goal': hydration.goal_volume,
        'percentage': min(int((hydration.current_volume / max(hydration.goal_volume, 1)) * 100), 100) if hydration.current_volume else 0
    }
    return render(request, 'logger/dashboard.html', context)

def add_water_api(request):
    if request.method == 'POST':
        today = timezone.localtime().date()
        hydration, created = DailyHydration.objects.get_or_create(date=today)
        hydration.current_volume += 250
        hydration.save()
        
        return JsonResponse({
            'status': 'success',
            'current_volume': hydration.current_volume,
            'goal': hydration.goal_volume,
            'percentage': min(int((hydration.current_volume / max(hydration.goal_volume, 1)) * 100), 100)
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def update_goal_api(request):
    if request.method == 'POST':
        today = timezone.localtime().date()
        hydration, created = DailyHydration.objects.get_or_create(date=today)
        new_goal = request.POST.get('goal_volume')
        if new_goal and new_goal.isdigit():
            hydration.goal_volume = int(new_goal)
            hydration.save()
            return JsonResponse({
                'status': 'success',
                'goal': hydration.goal_volume,
                'percentage': min(int((hydration.current_volume / max(hydration.goal_volume, 1)) * 100), 100)
            })
    return JsonResponse({'status': 'error'}, status=400)

def delete_workout_view(request, workout_id):
    if request.method == 'POST':
        workout = get_object_or_404(Workout, id=workout_id)
        workout.delete()
        
    next_url = request.GET.get('next')
    if next_url == 'history':
        return redirect('history')
    return redirect('dashboard')

def history_view(request):
    # order all workouts by date descending
    workouts = Workout.objects.all().order_by('-date', '-id')
    all_hydrations = DailyHydration.objects.all()
    
    hydrations_by_date = {h.date: h for h in all_hydrations}
    
    # group by date for display
    # we want to iterate over all distinct dates from both workouts and hydrations
    all_dates = set([w.date for w in workouts] + [h.date for h in all_hydrations])
    sorted_dates = sorted(list(all_dates), reverse=True)
    
    history_data = []
    for d in sorted_dates:
        d_workouts = [w for w in workouts if w.date == d]
        d_hydration = hydrations_by_date.get(d)
        history_data.append({
            'date': d,
            'workouts': d_workouts,
            'hydration': d_hydration
        })
        
    context = {
        'history_data': history_data
    }
    return render(request, 'logger/history.html', context)
