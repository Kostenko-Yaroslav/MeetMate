from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name

class Bell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bells')
    time_start = models.TimeField()
    time_end = models.TimeField()
    num = models.IntegerField()

    def __str__(self):
        return f"Bell {self.num} ({self.time_start} - {self.time_end})"

class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
    bell = models.ForeignKey(Bell, on_delete=models.CASCADE, related_name='lessons')

    class DayOfWeek(models.IntegerChoices):
        MONDAY = 0, 'Monday'
        TUESDAY = 1, 'Tuesday'
        WEDNESDAY = 2, 'Wednesday'
        THURSDAY = 3, 'Thursday'
        FRIDAY = 4, 'Friday'
        SATURDAY = 5, 'Saturday'
        SUNDAY = 6, 'Sunday'

    day_of_week = models.PositiveSmallIntegerField(
        choices=DayOfWeek.choices,
        default=DayOfWeek.MONDAY,
        verbose_name='Day of week'
    )

    def __str__(self):
        return f"Lesson {self.subject.name} {self.get_day_of_week_display()}"



