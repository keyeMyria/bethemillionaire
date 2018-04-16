from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.db.models import Q

from account.models import UserProfile
from .models import AffiliateLinkControl

from . import models
from account import models as account_model

from . import forms

"""
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())
        
    class Home(LoginRequiredMixin, View):
"""

class Home(View):
    template_name = 'home/index.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#affiliate link
class AffiliateLink(View):
    template_name = 'home/affiliate-link.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)
        affiliates = AffiliateLinkControl.objects.all()

        variables = {
            'user_profile': user_profile,
            'affiliates': affiliates,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


class EmailSwipes(View):
    template_name = 'home/email-swipes.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


class Banners(View):
    template_name = 'home/banners.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#dashboard - bitcoin basic --> WhatIsBitcoin
class WhatIsBitcoin(View):
    template_name = 'home/what-is-bitcoin.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#dashboard - bitcoin basic --> buy-bitcoins-here
class BuyBitcoinHere(View):
    template_name = 'home/buy-bitcoin-here.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#dashboard - bitcoin basic --> bitcoin-wallets
class BitcoinWallet(View):
    template_name = 'home/bitcoin-wallet.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#dashboard - bitcoin basic --> bitcoin-debit-card
class BitcoinDebitCard(View):
    template_name = 'home/bitcoin-debit-card.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass



#privacy policy
class PrivacyPolicy(View):
    template_name = 'home/privacy-policy.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#privacy policy
class FAQ(View):
    template_name = 'home/faq.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#privacy policy
class RecentUpdate(View):
    template_name = 'home/recent-update.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass



#privacy policy
class ManageTeam(View):
    template_name = 'home/manage-team.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        team_form = forms.TeamForm(request=request)

        my_referrals = request.user.referrals.all()

        teams = models.Team.objects.filter(owner=request.user)

        my_sponsor = request.user.sponsor
        sponsors_all_team = models.Team.objects.filter(owner=my_sponsor)

        my_join_teams = []

        for sponsor_team in sponsors_all_team:

            sponsors_team_member = sponsor_team.member.all()

            for sponsors_member in sponsors_team_member:
                if sponsors_member == request.user:
                    print("yes")
                    my_join_teams.append(sponsor_team)

        variables = {
            'user_profile': user_profile,
            'my_referrals': my_referrals,

            'tean_form': team_form,
            'teams': teams,

            'my_join_teams': my_join_teams,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        team_form = forms.TeamForm(request.POST or None, request=request)

        my_referrals = request.user.referrals.all()
        teams = models.Team.objects.filter(owner=request.user)

        if team_form.is_valid():
            team_form.deploy()

        variables = {
            'user_profile': user_profile,
            'my_referrals': my_referrals,

            'tean_form': team_form,
            'teams': teams,
        }

        return render(request, self.template_name, variables)




#add team member
class AddTeamMemberOperation(View):
    def get(self, request):
        new_member_id = request.GET.get('new_member')
        team_id = request.GET.get('team_id')

        team_obj = models.Team.objects.get(id=team_id)

        new_member_obj = account_model.UserProfile.objects.get(id=new_member_id)

        if team_obj.owner == request.user:
            models.Team.addMember(request.user, team_id, new_member_obj)
        else:
            pass

        return redirect('home:manage-team')


#remove team member
class RemoveTeamMemberOperation(View):
    def get(self, request):
        remove_member_id = request.GET.get('member_d')
        team_id = request.GET.get('team_id')

        team_obj = models.Team.objects.get(id=team_id)

        remove_member_obj = account_model.UserProfile.objects.get(id=remove_member_id)

        if team_obj.owner == request.user:
            models.Team.removeMember(request.user, team_id, remove_member_obj)
        else:
            pass

        return redirect('home:manage-team')




#personal training
class PersonalTraining(View):
    template_name = 'home/personal-training.html'

    def check_team_member(self, team, member):
        for team_member in team.member.all():
            if team_member == member:
                return True
            else:
                return False

    def get(self, request, owner_id, team_id):
        team = get_object_or_404(models.Team, id=team_id)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        owner = UserProfile.objects.get(id=owner_id)

        check_team_members = self.check_team_member(team, request.user)

        contents = None
        if check_team_members or owner == request.user:
            contents = models.PersonalTrainingContent.objects.filter(team=team)
        else:
            return redirect('home:manage-team')

        personal_training_form = None
        if owner == request.user:
            personal_training_form = forms.PersonalTrainingContentForm()

        variables = {
            'user_profile': user_profile,
            'owner': owner,
            'team': team,
            'personal_training_form': personal_training_form,

            'contents': contents,
        }

        return render(request, self.template_name, variables)

    def post(self, request, owner_id, team_id):
        team = get_object_or_404(models.Team, id=team_id)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        owner = UserProfile.objects.get(id=owner_id)

        personal_training_form = forms.PersonalTrainingContentForm(request.POST or None, request.FILES)

        if personal_training_form.is_valid():
            personal_training_form.deploy(owner, team)

        variables = {
            'user_profile': user_profile,
            'owner': owner,
            'personal_training_form': personal_training_form,
        }

        return render(request, self.template_name, variables)


