from django.views.generic import CreateView, TemplateView
from schedule.models import Subject, Bell, Lesson
from django.urls import reverse_lazy

from .forms import SubjectForm, BellForm, LessonForm

class CreateSchedulePage(TemplateView):
    template_name = "schedule/create_schedule.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subject_form"] = SubjectForm()
        context["bell_form"] = BellForm()
        context["lesson_form"] = LessonForm()
        return context

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    success_url =  reverse_lazy('schedule:create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BellCreateView(CreateView):
    model = Bell
    form_class = BellForm
    success_url = reverse_lazy('schedule:create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    success_url = reverse_lazy('schedule:create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
