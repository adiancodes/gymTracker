from django.db import models

class Workout(models.Model):
    exercise_type = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.exercise_type} - {self.sets}x{self.reps} on {self.date}"

class DailyHydration(models.Model):
    date = models.DateField(auto_now_add=True, unique=True)
    current_volume = models.IntegerField(default=0)

    def __str__(self):
        return f"Hydration for {self.date}: {self.current_volume}ml"
