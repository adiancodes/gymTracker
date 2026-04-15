import datetime
from django.shortcuts import render, redirect
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
        'goal': 2000,
        'percentage': min(int((hydration.current_volume / 2000) * 100), 100) if hydration.current_volume else 0
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
            'goal': 2000,
            'percentage': min(int((hydration.current_volume / 2000) * 100), 100)
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
