from huey.contrib.djhuey import periodic_task
from huey import crontab
from datetime import datetime
from schedule.models import Lesson
import webbrowser

@periodic_task(crontab(minute='*/1'))
def open_window():

    now = datetime.now()

    day_week = now.weekday()

    lessons = Lesson.objects.filter(bell__time_start__hour=now.hour, bell__time_start__minute=now.minute, day_of_week=day_week)

    for lesson in lessons:
        webbrowser.open(lesson.subject.link)