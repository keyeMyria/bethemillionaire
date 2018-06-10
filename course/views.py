from django.shortcuts import render
from django.views import View

from account.models import UserProfile
from lessons.models import Module, Lesson


class Course(View):
    template_name = 'course/course_v_3.html'

    def get(self, request):
        modules = Module.objects.all()
        lessons = Lesson.objects.all()

        variables = {
            'modules': modules,
            'lessons': lessons,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass
