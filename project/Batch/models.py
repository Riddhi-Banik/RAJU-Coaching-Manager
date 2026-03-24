from django.db import models
# Create your variables here.

weekdays_choice:list[tuple[str, str]] = [
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
]

# Create your models here.

class Batch(models.Model):
    name = models.CharField(max_length=31, unique = True)
    is_running = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Routine_part(models.Model):
    batch = models.ForeignKey(Batch, to_field = 'name', on_delete=models.CASCADE)
    weekday = models.CharField(max_length=10, choices= weekdays_choice, default='Friday')

    
