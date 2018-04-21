from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth.views import login, logout
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q
import datetime
from dateutil.relativedelta import relativedelta

from rest_framework.permissions import AllowAny

from . import models
from .models import UserProfile
from . import models
from .forms import LoginForm, RegistrationForm, UserEditForm, BasicInfoEditForm, PreregistrationForm, RegWebForm, MyRefferSearchForm
from . import serializers
from . import forms
from home.models import AffiliateLinkControl


#logout functionality
def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')


#pre registration
class Preregistration(View):
    template_name = 'account/preregistration.html'

    def get(self, request):
        form = PreregistrationForm()

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/pre-registration/?userid=admin')

        if affiliate_name:
            affiliate_db1 = models.BeTheMillionaire_3_Step_Registration_Funnel.objects.get(user__username=affiliate_name)
            affiliate_db1.visitors = affiliate_db1.visitors + 1
            affiliate_db1.save()
        else:
            affiliate_db1 = models.BeTheMillionaire_3_Step_Registration_Funnel.objects.get(user__username='admin')
            affiliate_db1.visitors = affiliate_db1.visitors + 1
            affiliate_db1.save()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        form = PreregistrationForm(request.POST or None)

        affiliate_name = request.GET.get("userid")

        if form.is_valid():
            form.preregistration(request)

            if affiliate_name == None:
                return HttpResponseRedirect("/account/registration/?userid=admin&s=%s" %('three'))
            else:
                return HttpResponseRedirect("/account/registration/?userid=%s&s=%s" %(affiliate_name, 'three'))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


#user login
class Login(View):
    template_name = 'account/login.html'

    def get(self, request):
        form = LoginForm()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        form = LoginForm(request.POST or None)

        s = request.GET.get('s')

        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)

                if s == 'welcome':
                    return redirect('topic:step_1')
                else:
                    return HttpResponseRedirect("/")
        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


#registration functionality
class Registration(View):
    template_name = 'account/registration.html'

    def get(self, request):
        affiliate_name = request.GET.get("userid")
        step = request.GET.get("s")

        if not affiliate_name:
            return HttpResponseRedirect('/account/registration/?userid=admin')


        form = RegistrationForm()

        if not step:
            if affiliate_name:
                affiliate_db2 = models.Direct_Registration.objects.get(user__username=affiliate_name)
                affiliate_db2.visitors = affiliate_db2.visitors + 1
                affiliate_db2.save()
            else:
                affiliate_db2 = models.Direct_Registration.objects.get(user__username='admin')
                affiliate_db2.visitors = affiliate_db2.visitors + 1
                affiliate_db2.save()


        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliate_name = request.GET.get("userid")
        step = request.GET.get("s")

        form = RegistrationForm(request.POST or None)

        if form.is_valid():
            user = form.registration(affiliate_name, step)

            if step == None:
                return redirect('account:welcome')
            elif step == 'three':
                return HttpResponseRedirect('/account/thank-you/?userid='+affiliate_name)
            else:
                return HttpResponseRedirect('/account/access/')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


#3rd affiliate - Automated Webinar Funnel Version 1
class PreWeb(View):
    template_name = 'account/pre-web.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-3')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        form = PreregistrationForm()

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/pre-web/?userid=admin')

        if affiliate_name:
            affiliate_db1 = models.Automated_Webinar_Funnel_Version_1.objects.get(user__username=affiliate_name)
            affiliate_db1.visitors = affiliate_db1.visitors + 1
            affiliate_db1.save()
        else:
            affiliate_db1 = models.Automated_Webinar_Funnel_Version_1.objects.get(user__username='admin')
            affiliate_db1.visitors = affiliate_db1.visitors + 1
            affiliate_db1.save()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-3')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        form = PreregistrationForm(request.POST or None)

        affiliate_name = request.GET.get("userid")

        if form.is_valid():
            form.preregistration(request)

            if affiliate_name == None:
                return HttpResponseRedirect("/account/reg-web/?userid=admin")
            else:
                return HttpResponseRedirect("/account/reg-web/?userid=%s" % affiliate_name)

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


class RegWeb(View):
    template_name = 'account/reg-web.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-3')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/reg-web/?userid=admin')

        form = RegWebForm()

        if not affiliate_name:
            return HttpResponseRedirect('/account/reg-web/?userid=admin')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-3')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = RegWebForm(request.POST or None)

        if form.is_valid():
            user = form.registration(affiliate_name)

            x = models.Automated_Webinar_Funnel_Version_1.objects.get(user__username=affiliate_name)
            x.leads = x.leads + 1
            x.save()

            return HttpResponseRedirect("/account/web-confirmation/?userid=%s" %(affiliate_name))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


class WebConfirmation(View):
    template_name = 'account/web-confirmation.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-3')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        form = PreregistrationForm()

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/web-confirmation/?userid=admin')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-3')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        form = PreregistrationForm(request.POST or None)

        affiliate_name = request.GET.get("userid")

        if form.is_valid():
            form.preregistration()

            if affiliate_name == None:
                return HttpResponseRedirect("/account/reg-web/?userid=admin")
            else:
                return HttpResponseRedirect("/account/reg-web/?userid=%s" %(affiliate_name))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


#end 3rd affiliate view :::::::::Automated Webinar Funnel Version 1:::::::::::::

#--4th affiliate view :::::::::Automated Webinar Funnel Version 2:::::::::::::
class Webinar(View):
    template_name = 'account/webinar.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-4')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        form = PreregistrationForm()

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/webinar/?userid=admin')

        if affiliate_name:
            affiliate_db1 = models.Automated_Webinar_Funnel_Version_2.objects.get(user__username=affiliate_name)
            affiliate_db1.visitors = affiliate_db1.visitors + 1
            affiliate_db1.save()
        else:
            affiliate_db1 = models.Automated_Webinar_Funnel_Version_2.objects.get(user__username='admin')
            affiliate_db1.visitors = affiliate_db1.visitors + 1
            affiliate_db1.save()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-4')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        form = PreregistrationForm(request.POST or None)

        affiliate_name = request.GET.get("userid")

        if form.is_valid():
            form.preregistration(request)

            if affiliate_name == None:
                return HttpResponseRedirect("/account/live-web-class/?userid=admin")
            else:
                return HttpResponseRedirect("/account/live-web-class/?userid=%s" %(affiliate_name))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


class LiveWebClass(View):
    template_name = 'account/live-web-class.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-4')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = RegWebForm()

        if not affiliate_name:
            return HttpResponseRedirect('/account/live-web-class/?userid=admin')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-4')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = RegWebForm(request.POST or None)

        if form.is_valid():
            user = form.registration(affiliate_name)

            x = models.Automated_Webinar_Funnel_Version_2.objects.get(user__username=affiliate_name)
            x.leads = x.leads + 1
            x.save()

            return HttpResponseRedirect("/account/watchlivewebclass/?userid=%s" %(affiliate_name))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


class WatchLiveWebClass(View):
    template_name = 'account/watchlivewebclass.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-4')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/watchlivewebclass/?userid=admin')

        if affiliate_name:
            sponsors = UserProfile.objects.filter(username=affiliate_name)
        else:
            sponsors = UserProfile.objects.filter(username='admin')

        variables = {
            'sponsors': sponsors,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass

#end 4th affiliate view :::::::::Automated Webinar Funnel Version 2:::::::::::::

#5th affiliate view :::::::::Course Giveaway Direct Registration:::::::::::::

class GetYourCourse(View):
    template_name = 'account/get-your-course.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-5')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = RegWebForm()

        if not affiliate_name:
            return HttpResponseRedirect('/account/get-your-course/?userid=admin')

        x = models.Course_Giveaway_Direct_Registration.objects.get(user__username=affiliate_name)
        x.visitors = x.visitors + 1
        x.save()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-5')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = RegWebForm(request.POST or None)

        if form.is_valid():
            user = form.registration(affiliate_name)

            x = models.Course_Giveaway_Direct_Registration.objects.get(user__username=affiliate_name)
            x.leads = x.leads + 1
            x.save()

            return HttpResponseRedirect("/account/access/?userid=%s" %(affiliate_name))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

#end 5th affiliate view :::::::::Course Giveaway Direct Registration:::::::::::::


#6th affiliate view :::::::::Course Giveaway 3 Steps Funnel:::::::::::::


class SecretsToWealth(View):
    template_name = 'account/secrets-to-wealth.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-6')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = PreregistrationForm()

        if not affiliate_name:
            return HttpResponseRedirect('/account/secrets-to-wealth/?userid=admin')

        x = models.Course_Giveaway_3_Steps_Funnel.objects.get(user__username=affiliate_name)
        x.visitors = x.visitors + 1
        x.save()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-6')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = PreregistrationForm(request.POST or None)

        if form.is_valid():
            user = form.preregistration(request)

            return HttpResponseRedirect("/account/secrets-to-wealth-final/?userid=%s" %(affiliate_name))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


class SecretsToWealthFinal(View):
    template_name = 'account/get-your-course.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-6')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = RegWebForm()

        if not affiliate_name:
            return HttpResponseRedirect('/secrets-to-wealth-final/?userid=admin')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-6')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = RegWebForm(request.POST or None)

        if form.is_valid():
            user = form.registration(affiliate_name)

            x = models.Course_Giveaway_3_Steps_Funnel.objects.get(user__username=affiliate_name)
            x.leads = x.leads + 1
            x.save()

            return HttpResponseRedirect("/account/access/?userid=%s" %(affiliate_name))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


#end 6th affiliate view :::::::::Course Giveaway 3 Steps Funnel:::::::::::::


#7th affiliate view :::::::::Latest Webinar Replay BTM:::::::::::::

class WebinarReplay(View):
    template_name = 'account/webinar-replay.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-7')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/webinar-replay/?userid=admin')

        x = models.Latest_Webinar_Replay_BTM.objects.get(user__username=affiliate_name)
        x.visitors = x.visitors + 1
        x.save()


        sponsors = UserProfile.objects.filter(username=affiliate_name)

        variables = {
            'sponsors': sponsors,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass

#end 7th affiliate view :::::::::Latest Webinar Replay BTM:::::::::::::


#end 8th affiliate view :::::::::Usi-Tech Funnel::::::::::::
class PreUsi(View):
    template_name = 'account/pre-usi.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-8')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = PreregistrationForm()

        if not affiliate_name:
            return HttpResponseRedirect('/account/pre-usi/?userid=admin')

        x = models.Usi_Tech_Funnel.objects.get(user__username=affiliate_name)
        x.visitors = x.visitors + 1
        x.save()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-8')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = PreregistrationForm(request.POST or None)

        if form.is_valid():
            user = form.preregistration(request)

            return HttpResponseRedirect("/account/reg-usi/?userid=%s" %(affiliate_name))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


class RegUsi(View):
    template_name = 'account/reg-usi.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-8')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = RegWebForm()

        if not affiliate_name:
            return HttpResponseRedirect('/account/reg-web/?userid=admin')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-8')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        form = RegWebForm(request.POST or None)

        if form.is_valid():
            user = form.registration(affiliate_name)

            x = models.Usi_Tech_Funnel.objects.get(user__username=affiliate_name)
            x.leads = x.leads + 1
            x.save()

            return HttpResponseRedirect("/account/usi-2/?userid=%s" %(affiliate_name))

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)


class Usi2(View):
    template_name = 'account/usi-2.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-8')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/usi-2/?userid=admin')

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


class UsiTechFastStart(View):
    template_name = 'account/usi-tech-fast-start.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-8')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/usi-tech-fast-start/?userid=admin')

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#end 8th affiliate view :::::::::Usi-Tech Funnel:::::::::::::


#9th affiliate view :::::::::Usi-Tech Direct Funnel:::::::::::::


class Usi(View):
    template_name = 'account/usi.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-9')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/usi/?userid=admin')

        x = models.Usi_Tech_Direct_Funnel.objects.get(user__username=affiliate_name)
        x.visitors = x.visitors + 1
        x.save()

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#end 9th affiliate view :::::::::Usi-Tech Direct Funnel:::::::::::::


#10th affiliate view :::::::::USI-TECH BTC-Packages Calculator:::::::::::::

#::::::::::::::::::::pending::::::::::::::::::::::::::::::

#end 10th affiliate view :::::::::USI-TECH BTC-Packages Calculator:::::::::::::


#11th affiliate view :::::::::Bitconnect Direct Funnel:::::::::::::
class Bitconnect(View):
    template_name = 'account/bitconnect.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-11')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/bitconnect/?userid=admin')

        x = models.Bitconnect_Direct_Funnel.objects.get(user__username=affiliate_name)
        x.visitors = x.visitors + 1
        x.save()

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


class BccFastStart(View):
    template_name = 'account/bcc-fast-start.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-11')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/bcc-fast-start/?userid=admin')

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#end 11th affiliate view :::::::::Bitconnect Direct Funnel:::::::::::::


#12th affiliate view :::::::::Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months):::::::::::::
class SevenFigureStrategies(View):
    template_name = 'account/seven-figure-strategies.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-12')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/7-figure-strategies/?userid=admin')

        x = models.Mike_Hobbs_Usi_Tech_Team_Webinar_90_bitcoins_in_6_months.objects.get(user__username=affiliate_name)
        x.visitors = x.visitors + 1
        x.save()

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass

#end 12th affiliate view :::::::::Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months):::::::::::::


#end 13th affiliate view :::::::::How To Set Up Your Bitcoins Wealth Club System:::::::::::::
class HowToSetUpYourBTMSystem(View):
    template_name = 'account/how-to-set-up-your-btm-system.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-13')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/how-to-set-up-your-btm-system/?userid=admin')

        x = models.How_To_Set_Up_Your_BeTheMillionaire_System.objects.get(user__username=affiliate_name)
        x.visitors = x.visitors + 1
        x.save()

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass

#end 13th affiliate view :::::::::How To Set Up Your Bitcoins Wealth Club System:::::::::::::


#14th affiliate view :::::::::usi tech 7 figure plan in 2018:::::::::::::
class SevenFigurePlan(View):
    template_name = 'account/seven-figure-plan.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.filter(short_name='affiliate-link-14')

        for affiliate in affiliates:
            if not affiliate.is_active:
                return HttpResponseRedirect('/account/registration/')

        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/7-figure-plan/?userid=admin')

        x = models.Usi_Tech_7_Figure_Plan_In_2018.objects.get(user__username=affiliate_name)
        x.visitors = x.visitors + 1
        x.save()

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#end 14th affiliate view :::::::::usi tech 7 figure plan in 2018:::::::::::::




#profile
class Profile(View):
    template_name = 'account/profile.html'

    def get(self, request):
        user_edit_form = UserEditForm(instance=UserProfile.objects.get(username=request.user.username))
        #basic_info_edit_form = BasicInfoEditForm(instance=UserProfile.objects.get(username=request.user.username))

        click_magic_form = forms.ClickMagicAccountEditForm(instance=models.ClickMagicAccount.objects.get(user=request.user))
        click_funnels_form = forms.ClickFunnelsAccountEditForm(instance=models.ClickFunnelsAccount.objects.get(user=request.user))
        getresponse_form = forms.GetResponseAccountEditForm(instance=models.GetResponseAccount.objects.get(user=request.user))
        aweber_form = forms.AweberAccountEditForm(instance=models.AweberAccount.objects.get(user=request.user))


        ledger_nano_s_form = forms.LedgerNanoSEditForm(instance=models.LedgerNanoSAccount.objects.get(user=request.user))
        trezor_s_form = forms.TrezorSEditForm(instance=models.TrezorSAccount.objects.get(user=request.user))
        coin_base_form = forms.CoinBaseEditForm(instance=models.CoinBaseAccount.objects.get(user=request.user))
        spectrocoin_card_form = forms.SpectrocoinCardEditForm(instance=models.SpectroCoinCardAccount.objects.get(user=request.user))
        cryptopay_card_form = forms.CryptoPayCardEditForm(instance=models.CryptoPayCardAccount.objects.get(user=request.user))
        cex_io_form = forms.CexIOEditForm(instance=models.CexIOAccount.objects.get(user=request.user))
        bitpanda_form = forms.BitPandaEditForm(instance=models.BitPandaAccount.objects.get(user=request.user))
        local_bitcoins_form = forms.LocalBitcoinsEditForm(instance=models.LocalBitcoinsAccount.objects.get(user=request.user))
        inda_coin_form = forms.IndaCoinEditForm(instance=models.IndaCoinAccount.objects.get(user=request.user))
        coin_mama_form = forms.CoinMamaEditForm(instance=models.CoinMamaAccount.objects.get(user=request.user))



        user_profiles = models.UserProfile.objects.filter(username=request.user.username)





        variables = {
            'user_edit_form': user_edit_form,
            #'basic_info_edit_form': basic_info_edit_form,

            'click_magic_form': click_magic_form,
            'click_funnels_form': click_funnels_form,
            'getresponse_form': getresponse_form,
            'aweber_form': aweber_form,

            'ledger_nano_s_form': ledger_nano_s_form,
            'trezor_s_form': trezor_s_form,
            'coin_base_form': coin_base_form,
            'spectrocoin_card_form': spectrocoin_card_form,
            'cryptopay_card_form': cryptopay_card_form,
            'cex_io_form': cex_io_form,
            'bitpanda_form': bitpanda_form,
            'local_bitcoins_form': local_bitcoins_form,
            'inda_coin_form': inda_coin_form,
            'coin_mama_form': coin_mama_form,


            'user_profiles': user_profiles,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        user_edit_form = UserEditForm(request.POST or None, request.FILES, instance=UserProfile.objects.get(username=request.user.username))

        click_magic_form = forms.ClickMagicAccountEditForm(request.POST or None, instance=models.ClickMagicAccount.objects.get(user=request.user))
        click_funnels_form = forms.ClickFunnelsAccountEditForm(request.POST or None, instance=models.ClickFunnelsAccount.objects.get(user=request.user))
        getresponse_form = forms.GetResponseAccountEditForm(request.POST or None, instance=models.GetResponseAccount.objects.get(user=request.user))
        aweber_form = forms.AweberAccountEditForm(request.POST or None, instance=models.AweberAccount.objects.get(user=request.user))


        ledger_nano_s_form = forms.LedgerNanoSEditForm(request.POST or None, instance=models.LedgerNanoSAccount.objects.get(user=request.user))
        trezor_s_form = forms.TrezorSEditForm(request.POST or None, instance=models.TrezorSAccount.objects.get(user=request.user))
        coin_base_form = forms.CoinBaseEditForm(request.POST or None, instance=models.CoinBaseAccount.objects.get(user=request.user))
        spectrocoin_card_form = forms.SpectrocoinCardEditForm(request.POST or None, instance=models.SpectroCoinCardAccount.objects.get(user=request.user))
        cryptopay_card_form = forms.CryptoPayCardEditForm(request.POST or None, instance=models.CryptoPayCardAccount.objects.get(user=request.user))
        cex_io_form = forms.CexIOEditForm(request.POST or None, instance=models.CexIOAccount.objects.get(user=request.user))
        bitpanda_form = forms.BitPandaEditForm(request.POST or None, instance=models.BitPandaAccount.objects.get(user=request.user))
        local_bitcoins_form = forms.LocalBitcoinsEditForm(request.POST or None, instance=models.LocalBitcoinsAccount.objects.get(user=request.user))
        inda_coin_form = forms.IndaCoinEditForm(request.POST or None, instance=models.IndaCoinAccount.objects.get(user=request.user))
        coin_mama_form = forms.CoinMamaEditForm(request.POST or None, instance=models.CoinMamaAccount.objects.get(user=request.user))


        user_profiles = models.UserProfile.objects.filter(username=request.user.username)


        if request.POST.get('account_info') == 'account_info':
            if user_edit_form.is_valid():
                user_edit_form.save()
                return redirect('account:profile')


        elif request.POST.get('click_magic') == 'click_magic':
            if click_magic_form.is_valid():
                click_magic_form.save()
                return redirect('account:profile')
        elif request.POST.get('click_funnels') == 'click_funnels':
            if click_funnels_form.is_valid():
                click_funnels_form.save()
                return redirect('account:profile')
        elif request.POST.get('getresponse') == 'getresponse':
            if getresponse_form.is_valid():
                getresponse_form.save()
                return redirect('account:profile')
        elif request.POST.get('aweber') == 'aweber':
            if aweber_form.is_valid():
                aweber_form.save()
                return redirect('account:profile')


        elif request.POST.get('ledger_nano_s') == 'ledger_nano_s':
            if ledger_nano_s_form.is_valid():
                ledger_nano_s_form.save()
                return redirect('account:profile')
        elif request.POST.get('trezor_s') == 'trezor_s':
            if trezor_s_form.is_valid():
                trezor_s_form.save()
                return redirect('account:profile')
        elif request.POST.get('coin_base') == 'coin_base':
            if coin_base_form.is_valid():
                coin_base_form.save()
                return redirect('account:profile')
        elif request.POST.get('spectro_coin_card') == 'spectro_coin_card':
            if spectrocoin_card_form.is_valid():
                spectrocoin_card_form.save()
                return redirect('account:profile')
        elif request.POST.get('cryptopay_card') == 'cryptopay_card':
            if cryptopay_card_form.is_valid():
                cryptopay_card_form.save()
                return redirect('account:profile')
        elif request.POST.get('cex_io') == 'cex_io':
            if cex_io_form.is_valid():
                cex_io_form.save()
                return redirect('account:profile')
        elif request.POST.get('bit_panda') == 'bit_panda':
            if bitpanda_form.is_valid():
                bitpanda_form.save()
                return redirect('account:profile')
        elif request.POST.get('local_bitcoins') == 'local_bitcoins':
            if local_bitcoins_form.is_valid():
                local_bitcoins_form.save()
                return redirect('account:profile')
        elif request.POST.get('inda_coin') == 'inda_coin':
            if inda_coin_form.is_valid():
                inda_coin_form.save()
                return redirect('account:profile')
        elif request.POST.get('coin_mama') == 'coin_mama':
            if coin_mama_form.is_valid():
                coin_mama_form.save()
                return redirect('account:profile')


        variables = {
            'user_edit_form': user_edit_form,

            'click_magic_form': click_magic_form,
            'click_funnels_form': click_funnels_form,
            'getresponse_form': getresponse_form,
            'aweber_form': aweber_form,

            'ledger_nano_s_form': ledger_nano_s_form,
            'trezor_s_form': trezor_s_form,
            'coin_base_form': coin_base_form,
            'spectrocoin_card_form': spectrocoin_card_form,
            'cryptopay_card_form': cryptopay_card_form,
            'cex_io_form': cex_io_form,
            'bitpanda_form': bitpanda_form,
            'local_bitcoins_form': local_bitcoins_form,
            'inda_coin_form': inda_coin_form,
            'coin_mama_form': coin_mama_form,

            'user_profiles': user_profiles,
        }

        return render(request, self.template_name, variables)


class MyReferrals(View):
    template_name = 'account/my-referrals.html'

    def get(self, request):
        form = MyRefferSearchForm()

        #--for search queries
        user_exists = False
        s_lists = ''
        if request.GET.get("userid"):
            s_user_id = request.GET.get("userid")

            user_exists = UserProfile.objects.filter(username=s_user_id).exists()

            if user_exists:
                s_referrals = UserProfile.objects.filter(Q(username=s_user_id) & Q(sponsor__username=request.user.username))

                s_referrals_referrals_count = []
                for s_referral in s_referrals:
                    s_referrals_username = s_referral.username

                    s_referrals_referrals = UserProfile.objects.filter(sponsor__username=s_referrals_username).count()
                    s_referrals_referrals_count.append(s_referrals_referrals)

                s_lists = zip(s_referrals, s_referrals_referrals_count)

        #--end search queries


        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_referrals = UserProfile.objects.filter(sponsor__username=request.user.username).count()

        referrals = UserProfile.objects.filter(sponsor__username=request.user.username)

        referrals_referrals_count = []
        for referral in referrals:
            username_referral = referral.username

            referrals_referrals = UserProfile.objects.filter(sponsor__username=username_referral).count()
            referrals_referrals_count.append(referrals_referrals)

        lists = zip(referrals, referrals_referrals_count)

        variables = {
            'user_profile': user_profile,
            'total_referrals': total_referrals,
            'lists': lists,
            'form': form,
            'user_exists': user_exists,
            's_lists': s_lists,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        form = MyRefferSearchForm(request.POST or None)
        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_referrals = UserProfile.objects.filter(sponsor__username=request.user.username).count()

        referrals = UserProfile.objects.filter(sponsor__username=request.user.username)

        referrals_referrals_count = []
        for referral in referrals:
            username_referral = referral.username

            referrals_referrals = UserProfile.objects.filter(sponsor__username=username_referral).count()
            referrals_referrals_count.append(referrals_referrals)

        lists = zip(referrals, referrals_referrals_count)

        if form.is_valid():
            username = form.cleaned_data.get("username")

            return HttpResponseRedirect('/account/membership-account/my-referrals/?userid=%s' %username)

        variables = {
            'user_profile': user_profile,
            'total_referrals': total_referrals,
            'lists': lists,
            'form': form,
        }

        return render(request, self.template_name, variables)


#public profile
class PublicProfile(View):
    template_name = 'account/public-profile.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        userid = request.GET.get("userid")

        if not userid:
            return HttpResponseRedirect('/account/membership-account/public-profile/?userid=admin')

        if userid:
            public_profiles = UserProfile.objects.filter(username=userid)

        variables = {
            'user_profile': user_profile,
            'public_profiles': public_profiles,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#access
class Access(View):
    template_name = 'account/access.html'

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        pass





#welcome page
class Welcome(View):
    template_name = 'account/welcome.html'

    def get(self, request):

        return render(request, self.template_name)



#thank you page
class ThankYou(View):
    template_name = 'account/thank-you.html'

    def get(self, request):
        affiliate_name = request.GET.get("userid")

        if not affiliate_name:
            return HttpResponseRedirect('/account/thank-you/?userid=admin')

        user = get_object_or_404(models.UserProfile, username=affiliate_name)

        coin_mama_account = models.CoinMamaAccount.objects.get(user=user)

        variables = {
            'coin_mama_account': coin_mama_account,
        }

        return render(request, self.template_name, variables)








#api view
class UserProfileAPI(APIView):
    def get(self, request):
        if request.GET.get("username"):
            username = request.GET.get("username")

            userObj = UserProfile.objects.filter(username=username)

            user_membership_name = None
            for user_membership in userObj:
                user_membership_name = user_membership.membership.name


            total_member = models.UserProfile.objects.all().count()


            serializer = None
            x = 'User authorized'

            if request.user.is_authenticated() and request.user.username == username:
                serializer = serializers.UserProfileSerializer(userObj, many=True).data
            else:
                x = 'Error authentication'

            return Response({
                'data': serializer,
                'x': x,
                'user_membership_name': user_membership_name,
                'total_member': total_member,
            })


#14 affiliate link api
class AffiliateLinkAPI(APIView):
    def get(self, request):
        if request.GET.get("username"):
            username = request.GET.get("username")

            userObj = UserProfile.objects.filter(username=username)

            #--14 affiliate object from model

            affiliate1 = models.BeTheMillionaire_3_Step_Registration_Funnel.objects.filter(user__username=username)
            affiliate2 = models.Direct_Registration.objects.filter(user__username=username)
            affiliate3 = models.Automated_Webinar_Funnel_Version_1.objects.filter(user__username=username)
            affiliate4 = models.Automated_Webinar_Funnel_Version_2.objects.filter(user__username=username)
            affiliate5 = models.Course_Giveaway_Direct_Registration.objects.filter(user__username=username)
            affiliate6 = models.Course_Giveaway_3_Steps_Funnel.objects.filter(user__username=username)
            affiliate7 = models.Latest_Webinar_Replay_BTM.objects.filter(user__username=username)
            affiliate8 = models.Usi_Tech_Funnel.objects.filter(user__username=username)
            affiliate9 = models.Usi_Tech_Direct_Funnel.objects.filter(user__username=username)
            affiliate10 = models.Usi_Tech_Btc_Packages_Calculator.objects.filter(user__username=username)
            affiliate11 = models.Bitconnect_Direct_Funnel.objects.filter(user__username=username)
            affiliate12 = models.Mike_Hobbs_Usi_Tech_Team_Webinar_90_bitcoins_in_6_months.objects.filter(user__username=username)
            affiliate13 = models.How_To_Set_Up_Your_BeTheMillionaire_System.objects.filter(user__username=username)
            affiliate14 = models.Usi_Tech_7_Figure_Plan_In_2018.objects.filter(user__username=username)

            serializer1 = None
            serializer2 = None
            serializer3 = None
            serializer4 = None
            serializer5 = None
            serializer6 = None
            serializer7 = None
            serializer8 = None
            serializer9 = None
            serializer10 = None
            serializer11 = None
            serializer12 = None
            serializer13 = None
            serializer14 = None
            x = 'User authorized'

            if request.user.is_authenticated() and request.user.username == username:
                serializer1 = serializers.BeTheMillionaire_3_Step_Registration_Funnel_Serializer(affiliate1, many=True).data
                serializer2 = serializers.Direct_Registration_Serializer(affiliate2, many=True).data
                serializer3 = serializers.Automated_Webinar_Funnel_Version_1_Serializer(affiliate3, many=True).data
                serializer4 = serializers.Automated_Webinar_Funnel_Version_2_Serializer(affiliate4, many=True).data
                serializer5 = serializers.Course_Giveaway_Direct_Registration_Serializer(affiliate5, many=True).data
                serializer6 = serializers.Course_Giveaway_3_Steps_Funnel_Serializer(affiliate6, many=True).data
                serializer7 = serializers.Latest_Webinar_Replay_BTM_Serializer(affiliate7, many=True).data
                serializer8 = serializers.Usi_Tech_Funnel_Serializer(affiliate8, many=True).data
                serializer9 = serializers.Usi_Tech_Direct_Funnel_Serializer(affiliate9, many=True).data
                serializer10 = serializers.Usi_Tech_Btc_Packages_Calculator_Serializer(affiliate10, many=True).data
                serializer11 = serializers.Bitconnect_Direct_Funnel_Serializer(affiliate11, many=True).data
                serializer12 = serializers.Mike_Hobbs_Usi_Tech_Team_Webinar_90_bitcoins_in_6_months_Serializer(affiliate12, many=True).data
                serializer13 = serializers.How_To_Set_Up_Your_BeTheMillionaire_System_Serializer(affiliate13, many=True).data
                serializer14 = serializers.Usi_Tech_7_Figure_Plan_In_2018_Serializer(affiliate14, many=True).data
            else:
                x = 'Error authentication'

            return Response({
                'serializer1': serializer1,
                'serializer2': serializer2,
                'serializer3': serializer3,
                'serializer4': serializer4,
                'serializer5': serializer5,
                'serializer6': serializer6,
                'serializer7': serializer7,
                'serializer8': serializer8,
                'serializer9': serializer9,
                'serializer10': serializer10,
                'serializer11': serializer11,
                'serializer12': serializer12,
                'serializer13': serializer13,
                'serializer14': serializer14,
                'x': x,
            })


#username check
def check_username(request):
    username = request.GET.get('userid')
    userExist = UserProfile.objects.filter(username=username).exists()

    if userExist:
        err_msg = "error"
    else:
        err_msg = "ok"

    data = {
        'err_msg': err_msg,
    }

    return JsonResponse(data)


class PaymentAPI(APIView):

    def get(self, request):
        if request.GET.get("payerID") and request.GET.get("paymentID") and request.GET.get("paymentToken") and request.GET.get("userid"):
            username = request.GET.get("userid")

            userObj = UserProfile.objects.get(username=username)
            intent = request.GET.get("intent")
            payerID = request.GET.get("payerID")
            paymentID = request.GET.get("paymentID")
            paymentToken = request.GET.get("paymentToken")
            membership_plan_id = request.GET.get("memberhsiplevel")
            membeshiplevelObj = models.Membershiplevel.objects.get(id=membership_plan_id)

            serializer = None
            x = 'User authorized'
            payment_confirm = 'unconfirmed'

            if request.user.is_authenticated() and request.user.username == username:
                deploy = models.Payment(user=userObj, intent=intent, payer_ID=payerID, payment_ID=paymentID, payment_Token=paymentToken, membership=membeshiplevelObj, is_verify='pending')
                deploy.save()
                payment_obj_id = deploy.id
                payment_date = deploy.creation_time

                #calculate expired date
                package_end_date = None
                if membeshiplevelObj.package == 'monthly':
                    package_end_date = payment_date + relativedelta(months=1)
                elif membeshiplevelObj.package == 'bi_annually':
                    package_end_date = payment_date + relativedelta(months=6)
                elif membeshiplevelObj.package == 'yearly':
                    package_end_date = payment_date + relativedelta(months=12)


                paymentObj = models.Payment.objects.get(id=payment_obj_id)

                paymentObj.expired_time = package_end_date
                paymentObj.save()

                #update user profile
                update_user_profile = UserProfile.objects.filter(username=username).update(membership=membeshiplevelObj, payments=paymentObj)

                payment_confirm = 'confirmed'

                serializer = serializers.PaymentSerializer(paymentObj, many=True).data
            else:
                x = 'Error authentication'
                payment_confirm = 'unconfirmed'

            return Response({
                'data': serializer,
                'x': x,
                'payment_confirm': payment_confirm,
            })
        else:
            return Response({
                'x': 'not permitted to view',
            })


#MyAutoresponderSettings
class MyAutoresponderSettings(View):
    template_name = 'account/my-auto-responder-settings.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        getresponseform = forms.GetResponseAutoresponderAddContactForm(instance=models.GetResponseAutoresponderAddContact.objects.get(user__username=request.user.username))


        get_response_accounts = models.GetResponseAccount.objects.get(user=request.user.sponsor)

        if get_response_accounts.getresponse_username:
            get_response_account = models.GetResponseAccount.objects.get(user=request.user.sponsor)

        else:
            get_response_account = models.GetResponseAccount.objects.get(user__username='admin')


        variables = {
            'user_profile': user_profile,
            'getresponseform': getresponseform,

            'get_response_account': get_response_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        getresponseform = forms.GetResponseAutoresponderAddContactForm(request.POST or None, instance=models.GetResponseAutoresponderAddContact.objects.get(user__username=request.user.username))

        if request.POST.get('getresponseform') == 'getresponseform':
            if getresponseform.is_valid():
                getresponseform.save()

        variables = {
            'user_profile': user_profile,
            'getresponseform': getresponseform,
        }

        return render(request, self.template_name, variables)


class MembershipLevels(View):
    template_name = 'account/membership-levels.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)


class MembershipCheckout(View):
    template_name = 'account/membership-checkout.html'

    def get(self, request):

        level = request.GET.get("level")
        name = request.GET.get("name")
        package = request.GET.get("package")

        membership_levels = models.Membershiplevel.objects.filter(Q(level=level) & Q(name=name) & Q(package=package))

        variables = {
            'membership_levels': membership_levels,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


class CheckoutSuccess(View):
    template_name = 'account/checkout-success.html'
    def get(self, request):
        return render(request, self.template_name)


class CheckoutFailure(View):
    template_name = 'account/checkout-failure.html'
    def get(self, request):
        return render(request, self.template_name)
