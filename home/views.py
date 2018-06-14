from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Count

from account.models import UserProfile
from .models import AffiliateLinkControl

from . import models
from account import models as account_model
from account import forms as account_form

from . import forms

from . import serializers

from administration import models as admin_model



from django.utils.safestring import mark_safe
import json


"""
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())
        
    class Home(LoginRequiredMixin, View):
"""


class Start(View):
    template_name = 'home/start.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass



class Home(View):
    template_name = 'home/index_v_3.html'

    def get(self, request):
        sponsor_teams = models.Team.objects.filter(owner=request.user.sponsor)
        total_member = account_model.UserProfile.objects.all().count()

        recent_update_posts = admin_model.RecentUpdatePost.objects.all().order_by('-date')[:5]

        webinar_registration_link = account_model.WebinarLink.objects.get(id=1)

        variables = {
            'sponsor_teams': sponsor_teams,
            'total_member': total_member,

            'webinar_registration_link': webinar_registration_link,

            'recent_update_posts': recent_update_posts,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass





#recent update post detail view
class RecentUpdatePostDetailView(View):
    template_name = 'home/recent-update-post-detail-view.html'

    def get(self, request, post_id):
        post = get_object_or_404(admin_model.RecentUpdatePost, id=post_id)

        variables = {
            'post': post,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass






#affiliate link
class AffiliateLink(View):
    template_name = 'home/affiliate-link_v_1.html'

    def get(self, request):
        affiliates = AffiliateLinkControl.objects.all()

        variables = {
            'affiliates': affiliates,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


class EmailSwipes(View):
    template_name = 'home/email-swipes_v_1.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


class Banners(View):
    template_name = 'home/banners_v_1.html'

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
    template_name = 'home/what-is-bitcoin_v_2.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#dashboard - bitcoin basic --> buy-bitcoins-here
class BuyBitcoinHere(View):
    template_name = 'home/buy-bitcoin-here_v_1.html'

    def get(self, request):
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
    template_name = 'home/bitcoin-wallet_v_2.html'

    def get(self, request):
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
            'ladger_nano_s_account': ladger_nano_s_account,
            'coin_base_account': coin_base_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#dashboard - bitcoin basic --> bitcoin-debit-card
class BitcoinDebitCard(View):
    template_name = 'home/bitcoin-debit-card_v_2.html'

    def get(self, request):

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
            'cryptocoin_account': cryptocoin_account,
            'spectrocoin_account': spectrocoin_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass



#privacy policy
class PrivacyPolicy(View):
    template_name = 'home/privacy-policy_v_1.html'

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
    template_name = 'home/faq_v_1.html'

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
    template_name = 'home/recent-update_v_1.html'

    def get(self, request):
        user_profile = UserProfile.objects.filter(username=request.user.username)

        variables = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass



#manage-team
class ManageTeam(View):
    template_name = 'home/manage-team_v_2.html'

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




#all team member
class AllTeamMember(View):
    template_name = 'home/all-team-member.html'

    def get(self, request, team_id):

        team = get_object_or_404(models.Team, id=team_id, owner=request.user)
        #team = models.Team.objects.get(Q(id=team_id) & Q(owner=request.user))

        team_members = team.member.all()

        variables = {
            'team': team,
            'team_members': team_members,
        }

        return render(request, self.template_name, variables)


    def post(self, request, team_id):
        team = get_object_or_404(models.Team, id=team_id, owner=request.user)
        #team = models.Team.objects.get(Q(id=team_id) & Q(owner=request.user))

        team_members = team.member.all()


        if request.POST.get('remove-team') == 'remove-team':
            team.delete()
            return redirect('home:manage-team')


        variables = {
            'team': team,
            'team_members': team_members,
        }

        return render(request, self.template_name, variables)




#add member to team
class AddMemberToTeam(View):
    template_name = 'home/add-member-to-team.html'

    def get(self, request, member_id):

        my_referrals = request.user.referrals.all()

        my_teams = models.Team.objects.filter(owner=request.user)

        member_obj = account_model.UserProfile.objects.get(id=member_id)


        if member_obj in my_referrals:
            member_obj = member_obj
        else:
            member_obj = None


        variables = {
            'my_teams': my_teams,

            'member_obj': member_obj,
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

        return redirect('account:my-referrals')


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

        return redirect('home:all-team-member', team_id=team_id)




#personal training
class PersonalTraining(View):
    template_name = 'home/personal-training_v_1.html'

    def check_team_member(self, team, member):
        for team_member in team.member.all():
            if team_member == member:
                return True
            else:
                return False

    def get(self, request, owner_id, team_id):
        team = get_object_or_404(models.Team, id=team_id)

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
            'owner': owner,
            'team': team,
            'personal_training_form': personal_training_form,

            'contents': contents,
        }

        return render(request, self.template_name, variables)

    def post(self, request, owner_id, team_id):
        team = get_object_or_404(models.Team, id=team_id)

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
            'owner': owner,
            'team': team,
            'personal_training_form': personal_training_form,

            'contents': contents,
        }

        return render(request, self.template_name, variables)


#passive income
class PassiveIncome(View):
    template_name = 'home/passive-income_v_2.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)


#crypto trading
class CryptoTrading(View):
    template_name = 'home/crypto-trading_v_1.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)


#crypto mining
class CryptoMining(View):
    template_name = 'home/crypto-mining_v_1.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)


#crypto resource
class CryptoResource(View):
    template_name = 'home/crypto-resource_v_1.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)



#crypto tools
class CryptoTool(View):
    template_name = 'home/crypto-tool_v_1.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)



#crypto tools
class HardwareWallet(View):
    template_name = 'home/hardware-wallet_v_1.html'

    def get(self, request):

        trezors_accounts = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        if trezors_accounts.trezor_username:
            trezors_account = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        else:
            trezors_account = account_model.TrezorSAccount.objects.get(user__username='admin')



        ladger_nano_s_accounts = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        if ladger_nano_s_accounts.ledger_nano_s_username:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        else:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user__username='admin')


        variables = {
            'trezors_account': trezors_account,
            'ladger_nano_s_account': ladger_nano_s_account,

        }

        return render(request, self.template_name, variables)



#social trading
class SocialTrading(View):
    template_name = 'home/social-trading_v_1.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)



#useful sides
class UsefulSide(View):
    template_name = 'home/useful-side_v_1.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)


#leader board

class LeaderBoard(View):
    template_name = 'home/leader-board_v_2.html'

    def get(self, request):

        leader_board_obj = admin_model.LeaderBoard.objects.all().last()

        if leader_board_obj:
            current_campaign_name = leader_board_obj.campaign_name
        else:
            current_campaign_name = ''
        
        members = admin_model.LeaderBoard.objects.filter(campaign_name=current_campaign_name).all()

        if members:
            campaign_date = members.first()
        else:
            campaign_date = None

        variables = {
            'members': members,
            'campaign_date': campaign_date,
        }

        return render(request, self.template_name, variables)




#Payment account settings
class PaymentAccountSetting(View):
    template_name = 'home/payment-account-setting_v_2.html'

    def get(self, request):

        current_payment_account = models.PaymentAccountSetting.objects.filter(user=request.user)

        payment_account_form = forms.PaymentAccountSettingForm()

        variables = {
            'payment_account_form': payment_account_form,
            'current_payment_account': current_payment_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        current_payment_account = models.PaymentAccountSetting.objects.filter(user=request.user)

        payment_account_form = forms.PaymentAccountSettingForm(request.POST or None)

        if payment_account_form.is_valid():
            payment_account_form.deploy(request)

        variables = {
            'payment_account_form': payment_account_form,
            'current_payment_account': current_payment_account,
        }

        return render(request, self.template_name, variables)



#my commission
class MyCommission(View):
    template_name = 'home/my-commission_v_2.html'

    def get(self, request):

        commissions = account_model.ReferralSaleCommission.objects.filter(user=request.user).order_by('is_verified')

        variables = {
            'commissions': commissions,
        }

        return render(request, self.template_name, variables)




#live
class Live(View):
    template_name = 'home/live.html'

    def get(self, request, room_name):

        db_room_name = 'chat_%s' %(room_name)

        path = request.get_full_path()

        variables = {
            'room_name_json': mark_safe(json.dumps(room_name)),
            'db_room_name': db_room_name,
            'room_name': room_name,

            'path': path,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass



def room(request, room_name):
    return render(request, 'home/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })




#api view
class LiveChatMessageAPI(APIView):
    def get(self, request, room_name):

        serializer = None
        x = 'User authorized'

        """
        if request.user.is_authenticated():
            message_obj = models.LiveChatMessage.objects.filter(room=room_name)
            serializer = serializers.LiveChatMessageSerializers(message_obj, many=True).data
        else:
            x = 'Error authentication'
        """

        message_obj = models.LiveChatMessage.objects.filter(room=room_name)
        serializer = serializers.LiveChatMessageSerializers(message_obj, many=True).data


        return Response({
            'data': serializer,
            'x': x,
        })
