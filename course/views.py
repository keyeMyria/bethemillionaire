from django.shortcuts import render
from django.views import View

from account.models import UserProfile
from lessons.models import Module, Lesson


class Course(View):
    template_name = 'course/course.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)
        modules = Module.objects.all()
        lessons = Lesson.objects.all()

        variables = {
            'user_profile': user_profile,
            'modules': modules,
            'lessons': lessons,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass
