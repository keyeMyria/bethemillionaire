from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin

from lessons.models import Module, Lesson, Step
from home.models import AffiliateLinkControl
from topic.models import StepControl

from . import forms


class AdminPermission(PermissionRequiredMixin, View):
    permission_required = 'is_superuser'


class Index(AdminPermission, View):
    template_name = 'administration/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass


#module control view
class ModuleControl(AdminPermission, View):
    template_name = 'administration/module-control.html'

    def get(self, request):

        modules = Module.objects.all()

        variables = {
            'modules': modules,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        modules = Module.objects.all()

        module_id = request.POST.get('module_id')
        module_action = request.POST.get('module_action')

        if module_action == 'disable':
            change_state = Module.objects.filter(id=module_id).update(is_active=False)

            module_obj = Module.objects.get(id=module_id)

            lessons = Lesson.objects.filter(module=module_obj)

            for lesson in lessons:
                lesson.is_active = False
                lesson.save()

        if module_action == 'active':
            change_state = Module.objects.filter(id=module_id).update(is_active=True)
            module_obj = Module.objects.get(id=module_id)

            lessons = Lesson.objects.filter(module=module_obj)

            for lesson in lessons:
                lesson.is_active = True
                lesson.save()

        variables = {
            'modules': modules,
        }

        return render(request, self.template_name, variables)


#lesson control view
class LessonControl(AdminPermission, View):
    template_name = 'administration/lesson-control.html'

    def get(self, request):
        modules = Module.objects.all()

        variables = {
            'modules': modules,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#lesson detail view
class LessonDetail(AdminPermission, View):
    template_name = 'administration/lesson-detail.html'

    def get(self, request, module_id):

        modules = Module.objects.filter(id=module_id)

        lessons = Lesson.objects.filter(module=modules).all()

        variables = {
            'modules': modules,
            'lessons': lessons,
        }

        return render(request, self.template_name, variables)

    def post(self, request, module_id):
        modules = Module.objects.filter(id=module_id)
        lessons = Lesson.objects.filter(module=modules).all()

        lesson_id = request.POST.get('lesson_id')
        lesson_action = request.POST.get('lesson_action')

        print(lesson_id, lesson_action)

        if lesson_action == 'disable':
            change_state = Lesson.objects.filter(id=lesson_id).update(is_active=False)

        if lesson_action == 'active':
            change_state = Lesson.objects.filter(id=lesson_id).update(is_active=True)

        variables = {
            'modules': modules,
            'lessons': lessons,
        }

        return render(request, self.template_name, variables)


#affiliate link control
class AffiliateLinkControls(AdminPermission, View):
    template_name = 'administration/affiliate-link-control.html'

    def get(self, request):

        affiliates = AffiliateLinkControl.objects.all()

        variables = {
            'affiliates': affiliates,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.all()

        link_id = request.POST.get('link_id')
        link_action = request.POST.get('link_action')

        if link_action == 'disable':
            change_state = AffiliateLinkControl.objects.filter(id=link_id).update(is_active=False)

        if link_action == 'active':
            change_state = AffiliateLinkControl.objects.filter(id=link_id).update(is_active=True)

        variables = {
            'affiliates': affiliates,
        }

        return render(request, self.template_name, variables)


#step control
class StepControls(AdminPermission, View):
    template_name = 'administration/step-control.html'

    def get(self, request):

        steps = StepControl.objects.all()

        variables = {
            'steps': steps,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        steps = StepControl.objects.all()

        step_id = request.POST.get('step_id')
        step_action = request.POST.get('step_action')

        if step_action == 'disable':
            change_state = StepControl.objects.filter(id=step_id).update(is_active=False)

        if step_action == 'active':
            change_state = StepControl.objects.filter(id=step_id).update(is_active=True)

        variables = {
            'steps': steps,
        }

        return render(request, self.template_name, variables)



#lesson control view
class AddVideo(AdminPermission, View):
    template_name = 'administration/add-video.html'

    def get(self, request):
        form = forms.VideoLinkForm()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        form = forms.VideoLinkForm(request.POST or None)

        if form.is_valid():
            form.deploy()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)
