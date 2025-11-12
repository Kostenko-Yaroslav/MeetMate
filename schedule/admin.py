from django.contrib import admin

from schedule.models import Bell, Subject, Lesson

admin.site.register(Subject)
admin.site.register(Bell)
admin.site.register(Lesson)
