from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.db.models import Q

from account.models import UserProfile
from .models import AffiliateLinkControl

from . import models
from account import models as account_model
from account import forms as account_form

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

        itb_form = account_form.ITBEditForm(instance=account_model.ITBAccount.objects.get(user=request.user))

        click_magic_form = account_form.ClickMagicAccountEditForm(instance=account_model.ClickMagicAccount.objects.get(user=request.user))


        itb_accounts = account_model.ITBAccount.objects.get(user=request.user.sponsor)

        if itb_accounts.itb_username:
            itb_account = account_model.ITBAccount.objects.get(user=request.user.sponsor)

        else:
            itb_account = account_model.ITBAccount.objects.get(user__username='admin')


        click_magic_accounts = account_model.ClickMagicAccount.objects.get(user=request.user.sponsor)

        if click_magic_accounts.clickmagic_username:
            click_magic_account = account_model.ClickMagicAccount.objects.get(user=request.user.sponsor)

        else:
            click_magic_account = account_model.ClickMagicAccount.objects.get(user__username='admin')



        variables = {
            'user_profile': user_profile,

            'itb_form': itb_form,
            'click_magic_form': click_magic_form,

            'itb_account': itb_account,
            'click_magic_account': click_magic_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        itb_form = account_form.ITBEditForm(request.POST or None, instance=account_model.ITBAccount.objects.get(user=request.user))

        click_magic_form = account_form.ClickMagicAccountEditForm(request.POST or None, instance=account_model.ClickMagicAccount.objects.get(user=request.user))

        if request.POST.get('itb_account') == 'itb_account':
            if itb_form.is_valid():
                itb_form.save()

        elif request.POST.get('click_magic_account') == 'click_magic_account':
            if click_magic_form.is_valid():
                click_magic_form.save()

        variables = {
            'user_profile': user_profile,

            'itb_form': itb_form,
            'click_magic_form': click_magic_form,
        }

        return render(request, self.template_name, variables)



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

        coin_mama_accounts = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        if coin_mama_accounts.coin_mama_username:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        else:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user__username='admin')


        coin_base_accounts = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        if coin_base_accounts.coinbase_username:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        else:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user__username='admin')


        cex_io_accounts = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        if cex_io_accounts.cexio_username:
            cex_io_account = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        else:
            cex_io_account = account_model.CexIOAccount.objects.get(user__username='admin')


        bit_panda_accounts = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        if bit_panda_accounts.bitpanda_username:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        else:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user__username='admin')


        inda_coin_accounts = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        if inda_coin_accounts.indacoin_username:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        else:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user__username='admin')


        local_bitcoin_accounts = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        if local_bitcoin_accounts.local_bitcoins_username:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        else:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user__username='admin')


        variables = {
            'user_profile': user_profile,

            'coin_mama_account': coin_mama_account,
            'coin_base_account': coin_base_account,
            'cex_io_account': cex_io_account,
            'bit_panda_account': bit_panda_account,
            'inda_coin_account': inda_coin_account,
            'local_bitcoin_account': local_bitcoin_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#dashboard - bitcoin basic --> bitcoin-wallets
class BitcoinWallet(View):
    template_name = 'home/bitcoin-wallet.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        ladger_nano_s_accounts = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        if ladger_nano_s_accounts.ledger_nano_s_username:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        else:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user__username='admin')


        coin_base_accounts = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        if coin_base_accounts.coinbase_username:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        else:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user__username='admin')


        variables = {
            'user_profile': user_profile,

            'ladger_nano_s_account': ladger_nano_s_account,
            'coin_base_account': coin_base_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#dashboard - bitcoin basic --> bitcoin-debit-card
class BitcoinDebitCard(View):
    template_name = 'home/bitcoin-debit-card.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        cryptocoin_accounts = account_model.CryptoPayCardAccount.objects.get(user=request.user.sponsor)

        if cryptocoin_accounts.cryptopay_card_username:
            cryptocoin_account = account_model.CryptoPayCardAccount.objects.get(user=request.user.sponsor)

        else:
            cryptocoin_account = account_model.CryptoPayCardAccount.objects.get(user__username='admin')


        spectrocoin_accounts = account_model.SpectroCoinCardAccount.objects.get(user=request.user.sponsor)

        if spectrocoin_accounts.spectrocoin_card_username:
            spectrocoin_account = account_model.SpectroCoinCardAccount.objects.get(user=request.user.sponsor)

        else:
            spectrocoin_account = account_model.SpectroCoinCardAccount.objects.get(user__username='admin')


        variables = {
            'user_profile': user_profile,

            'cryptocoin_account': cryptocoin_account,
            'spectrocoin_account': spectrocoin_account,
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

        my_sponsor = request.user.sponsor
        sponsors_all_team = models.Team.objects.filter(owner=my_sponsor)

        my_join_teams = []

        for sponsor_team in sponsors_all_team:

            sponsors_team_member = sponsor_team.member.all()

            for sponsors_member in sponsors_team_member:
                if sponsors_member == request.user:
                    print("yes")
                    my_join_teams.append(sponsor_team)

        if team_form.is_valid():
            team_form.deploy()

        variables = {
            'user_profile': user_profile,
            'my_referrals': my_referrals,

            'tean_form': team_form,
            'teams': teams,

            'my_join_teams': my_join_teams,
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

        check_team_members = self.check_team_member(team, request.user)

        contents = None
        if check_team_members or owner == request.user:
            contents = models.PersonalTrainingContent.objects.filter(team=team)
        else:
            return redirect('home:manage-team')

        personal_training_form = None
        if owner == request.user:
            personal_training_form = forms.PersonalTrainingContentForm(request.POST or None, request.FILES)
            if personal_training_form.is_valid():
                personal_training_form.deploy(owner, team)

        variables = {
            'user_profile': user_profile,
            'owner': owner,
            'team': team,
            'personal_training_form': personal_training_form,

            'contents': contents,
        }

        return render(request, self.template_name, variables)


#passive income
class PassiveIncome(View):
    template_name = 'home/passive-income.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


from django.db.models import Count

#leader board
class LeaderBoard(View):
    template_name = 'home/leader-board.html'

    def get(self, request):
        members = account_model.UserProfile.objects.annotate(refer_count=Count('referrals')).order_by('-refer_count')[:15]

        variables = {
            'members': members,
        }

        return render(request, self.template_name, variables)




