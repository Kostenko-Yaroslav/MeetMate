from huey.contrib.djhuey import periodic_task
from huey import crontab
from datetime import datetime
from schedule.models import Lesson
import time
from bot.bot_instance import bot

import urllib.request, json

@periodic_task(crontab(minute='*/1'))
def open_window():

    now = datetime.now()

    day_week = now.weekday()

    lessons = Lesson.objects.select_related("user", "subject", "bell").filter(day_of_week=day_week)

    lesson_start = lessons.filter(bell__time_start__hour=now.hour, bell__time_start__minute=now.minute)
    lesson_end = lessons.filter(bell__time_end__hour=now.hour, bell__time_end__minute=now.minute)

    try:
        with urllib.request.urlopen('https://ubilling.net.ua/aerialalerts/') as url:
            data = json.loads(url.read().decode())
    except:
        data = None

    def lesson_message(lesson, is_start):
        try:
            if hasattr(lesson.user, 'profile' and lesson.user.profile.chat_id):
                pass

            chat_id = lesson.user.profile.chat_id

            if lesson.user.profile.city in data['states']:
                alert_status = data['states'][lesson.user.profile.city]['alertnow']
            else:
                alert_status = False


            if alert_status:
                text = f'Тревога!'
            else:
                if is_start:
                    text = f'Пара: {lesson.subject.name} НАЧАЛАСЬ ! Link: {lesson.subject.link};'
                else:
                    text = f'Пара: {lesson.subject.name} ЗАКОНЧИЛАСЬ ! Link: {lesson.subject.link};'
            profile = lesson.user.profile.repeats

            for _ in range(profile):
                bot.send_message(chat_id, text)
                time.sleep(1)

        except Exception as e:
            print(e)

    for lesson in lesson_start:
        lesson_message(lesson, is_start=True)

    for lesson in lesson_end:
        lesson_message(lesson, is_start=False)