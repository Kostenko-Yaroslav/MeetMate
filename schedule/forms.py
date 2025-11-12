from django.forms import ModelForm
from schedule.models import Subject, Bell, Lesson

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'link']

class BellForm(ModelForm):
    class Meta:
        model = Bell
        fields = ['time_start', 'time_end','num']

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'bell', 'day_of_week']