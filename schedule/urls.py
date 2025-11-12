from django.urls import path

from schedule.views import CreateSchedulePage, SubjectCreateView, BellCreateView, LessonCreateView

app_name = 'schedule'
urlpatterns = [
    path('create/', CreateSchedulePage.as_view(), name='create'),
    path('create/subject/', SubjectCreateView.as_view(), name='create_subject'),
    path('create/bell/', BellCreateView.as_view(), name='create_bell'),
    path('create/lesson', LessonCreateView.as_view(), name='create_lesson'),
]