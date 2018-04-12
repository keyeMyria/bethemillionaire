from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin

import datetime
from dateutil.relativedelta import relativedelta

from lessons.models import Module, Lesson, Step
from home.models import AffiliateLinkControl
from topic.models import StepControl

from account import models as account_model
from account import forms as account_form

from . import forms


class AdminPermission(PermissionRequiredMixin, View):
    permission_required = 'is_superuser'


class Index(AdminPermission, View):
    template_name = 'administration/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass



#all user
class AllUser(AdminPermission, View):
    template_name = 'administration/all-user.html'

    def get(self, request):

        all_users = account_model.UserProfile.objects.all()
        all_users_count = account_model.UserProfile.objects.all().count()

        variables = {
            'all_users': all_users,
            'all_users_count': all_users_count,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass



#user detail
class UserDetail(AdminPermission, View):
    template_name = 'administration/user-detail.html'

    def get(self, request, user_id):

        user = get_object_or_404(account_model.UserProfile, pk=user_id)

        payments = account_model.Payment.objects.filter(user__id=user_id).order_by('-creation_time')


        package_end_date = None
        package_start_date = None
        p_start_date = None
        if user.membership.name != 'free':
            p_start_date = user.package_buy_time

            package_start_date = p_start_date

            package_end_date = None

            if user.membership.package == 'monthly':
                package_end_date = package_start_date + relativedelta(months=1)
            elif user.membership.package == 'bi_annually':
                package_end_date = package_start_date + relativedelta(months=6)
            elif user.membership.package == 'yearly':
                package_end_date = package_start_date + relativedelta(months=12)


        variables = {
            'user': user,
            'payments': payments,
            'p_start_date': p_start_date,
            'package_end_date': package_end_date,
        }

        return render(request, self.template_name, variables)

    def post(self, request, user_id):
        pass



#edit user
class EditUser(AdminPermission, View):
    template_name = 'administration/user-edit.html'

    def get(self, request, user_id):

        user = get_object_or_404(account_model.UserProfile, pk=user_id)

        user_edit_form = account_form.UserEditForm(instance=account_model.UserProfile.objects.get(id=user_id))

        variables = {
            'user': user,
            'user_edit_form': user_edit_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request, user_id):
        user = get_object_or_404(account_model.UserProfile, pk=user_id)

        user_edit_form = account_form.UserEditForm(request.POST or None, request.FILES, instance=account_model.UserProfile.objects.get(id=user_id))

        if user_edit_form.is_valid():
            user_edit_form.save()

            return redirect('administration:user-detail', user_id=user.id)

        variables = {
            'user': user,
            'user_edit_form': user_edit_form,
        }

        return render(request, self.template_name, variables)



#change user password
class ChangeUserPassword(View):
    template_name = 'administration/change-user-password.html'

    def get(self, request, user_id):

        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)

        change_user_password = forms.ChangeUserPasswordForm()

        variables = {
            'users': users,
            'change_user_password': change_user_password,
        }

        return render(request, self.template_name, variables)

    def post(self, request, user_id):
        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)

        change_user_password = forms.ChangeUserPasswordForm(request.POST or None)

        if change_user_password.is_valid():
            change_user_password.deploy(user_id)

        variables = {
            'users': users,
            'change_user_password': change_user_password,
        }

        return render(request, self.template_name, variables)




#active or deactive user
class ActiveDeactiveUser(AdminPermission, View):
    template_name = 'administration/activate-deactivate-user.html'

    def get(self, request, profile_status, user_id):

        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)

        variables = {
            'users': users,
            'profile_status': profile_status,
        }

        return render(request, self.template_name, variables)

    def post(self, request, profile_status, user_id):
        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)

        if request.POST.get('yes') == 'yes':
            for user in users:
                if profile_status == 'activate':
                    user.is_active = True
                    user.save()
                elif profile_status == 'deactivate':
                    user.is_active = False
                    user.save()
            return redirect('administration:user-detail', user_id=user_id)

        elif request.POST.get('no') == 'no':
            return redirect('administration:user-detail', user_id=user_id)


        variables = {
            'users': users,
            'profile_status': profile_status,
        }

        return render(request, self.template_name, variables)




#delete user
class DeleteUser(AdminPermission, View):
    template_name = 'administration/delete-user.html'

    def get(self, request, user_id):

        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)

        variables = {
            'users': users,
        }

        return render(request, self.template_name, variables)

    def post(self, request, user_id):
        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)

        if request.POST.get('yes') == 'yes':
            users.delete()
            return redirect('administration:all-user')

        elif request.POST.get('no') == 'no':
            return redirect('administration:all-user')

        variables = {
            'users': users,
        }

        return render(request, self.template_name, variables)



#change membership
class ChangeMembership(AdminPermission, View):
    template_name = 'administration/change-membership.html'

    def get(self, request, user_id):

        user = get_object_or_404(account_model.UserProfile, pk=user_id)

        change_membership_form = forms.ChangeMembershipForm(instance=account_model.UserProfile.objects.get(id=user_id))

        variables = {
            'user': user,
            'change_membership_form': change_membership_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request, user_id):
        user = get_object_or_404(account_model.UserProfile, pk=user_id)

        change_membership_form = forms.ChangeMembershipForm(request.POST or None, instance=account_model.UserProfile.objects.get(id=user_id))

        if change_membership_form.is_valid():
            change_membership_form.save()

            user_obj = account_model.UserProfile.objects.get(id=user_id)
            user_obj.package_buy_time = datetime.datetime.now()
            user_obj.save()

            return redirect('administration:user-detail', user_id=user.id)

        variables = {
            'user': user,
            'change_membership_form': change_membership_form,
        }

        return render(request, self.template_name, variables)






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
