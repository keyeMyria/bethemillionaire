from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re
import itertools
from django.contrib.auth.forms import PasswordChangeForm

from . import tasks

from .models import UserProfile, Preregistration, BeTheMillionaire_3_Step_Registration_Funnel, Direct_Registration

from . import models

import requests
import simplejson
import socket


def add_contact_getresponse(user_id, email, username):
    getresponseExists = models.GetResponseAutoresponderAddContact.objects.filter(user__username=user_id).exists()

    if getresponseExists:
        getresponseObj = models.GetResponseAutoresponderAddContact.objects.filter(user__username=user_id)

        if username == None:
            username = ''
        else:
            username = username

        for getresponseUser in getresponseObj:
            campaign_id = getresponseUser.campaignId
            api_key = getresponseUser.api_key
            isEnable = getresponseUser.isEnable

            if isEnable.upper() == 'ENABLE':
                ipaddress = socket.gethostbyname(socket.gethostname())

                c = {
                        'campaignId': campaign_id,
                    }

                data = {
                    'name': username,
                    'email': email,
                    'dayOfCycle': 0,
                    'campaign': c,
                    'ipAddress': ipaddress,
                }

                data_json = simplejson.dumps(data)

                api_format = 'api-key %s' %api_key

                headers = {
                    'Content-Type': 'application/json',
                    'X-Auth-Token': api_format,
                }

                r = requests.post('https://api.getresponse.com/v3/contacts', headers=headers, data=data_json)

            else:
                print("Get Response not enabled")
    else:
        print("False")


#email registration / pre-registration
class PreregistrationForm(forms.Form):
    email = forms.EmailField(max_length=100, required=False)

    def clean(self):
        email = self.cleaned_data.get("email")

        if len(email) < 1:
            raise forms.ValidationError("Enter Email Address")
        else:
            email_correction = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

            if email_correction == None:
                raise forms.ValidationError("Email Address not correct!")

    def preregistration(self, request):
        email = self.cleaned_data.get("email")

        deploy = Preregistration(email=email)
        deploy.save()

        #getresponse autoresponder add contact

        add_contact_getresponse(request.GET.get('userid'), email, 'None')
        add_contact_getresponse('Mena', email, 'None')

        #end getresponse autoresponder add contact


#registration form
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix'}))
    email = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'email'}))
    password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate',}))
    password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password'}))

    def check_space(self, username):
        for x in username:
            if x == ' ':
                return True

        return False

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if len(username) < 1:
            raise forms.ValidationError("Enter username!")
        else:
            check_username_space = self.check_space(username)

            if check_username_space:
                raise forms.ValidationError('You can not use space in username!')
            else:
                user_exist = UserProfile.objects.filter(username__iexact=username).exists()
                if user_exist:
                    raise forms.ValidationError("Username already taken!")
                else:
                    if len(email) < 1:
                        raise forms.ValidationError("Enter email address!")
                    else:
                        email_correction = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', email)
                        if email_correction == None:
                            raise forms.ValidationError("Email not correct!")
                        else:
                            email_exist = UserProfile.objects.filter(email__iexact=email).exists()
                            if email_exist:
                                raise forms.ValidationError("Email already exist!")
                            else:
                                if len(password1) < 8:
                                    raise forms.ValidationError("Password is too short!")
                                else:
                                    if password1 != password2:
                                        raise forms.ValidationError("Password not matched!")

    def registration(self, user_id=None, step=None):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')

        if user_id == None:
            sponsor_obj = UserProfile.objects.get(username='Mena')

            user = UserProfile(username=username, email=email, sponsor=sponsor_obj)
            user.set_password(password1)
            user.save()

            #celery task
            tasks.sent_registration_email.delay(sponsor_obj.username, sponsor_obj.email, username, email)
            tasks.sent_registred_email.delay(username, email, password1)

            #add referral
            current_user = UserProfile.objects.get(id=user.id)

            UserProfile.addReferral('Mena', current_user)

            #update lead
            if step == None:
                x = models.Direct_Registration.objects.get(user__username='Mena')
                x.leads = x.leads + 1
                x.save()
            elif step == 'three':
                x = BeTheMillionaire_3_Step_Registration_Funnel.objects.get(user__username='Mena')
                x.leads = x.leads + 1
                x.save()


            #getresponse autoresponder add contact

            add_contact_getresponse(sponsor_obj.username, email, username)
            add_contact_getresponse('Mena', email, username)

            #end getresponse autoresponder add contact

        else:
            sponsor_obj = UserProfile.objects.get(username=user_id)

            user = UserProfile(username=username, email=email, sponsor=sponsor_obj)
            user.set_password(password1)
            user.save()

            #celery task
            tasks.sent_registration_email.delay(sponsor_obj.username, sponsor_obj.email, username, email)
            tasks.sent_registred_email.delay(username, email, password1)

            current_user = UserProfile.objects.get(id=user.id)

            UserProfile.addReferral(user_id, current_user)

            current_user_obj = UserProfile.objects.filter(id=user.id).update(sponsor=sponsor_obj)

            #update lead
            if step == None:
                x = models.Direct_Registration.objects.get(user__username=user_id)
                x.leads = x.leads + 1
                x.save()
            elif step == 'three':
                x = models.BeTheMillionaire_3_Step_Registration_Funnel.objects.get(user__username=user_id)
                x.leads = x.leads + 1
                x.save()



            #getresponse autoresponder add contact

            add_contact_getresponse(sponsor_obj.username, email, username)
            add_contact_getresponse('Mena', email, username)

            #end getresponse autoresponder add contact



        return user


#my reffer page search using username
class MyRefferSearchForm(forms.Form):
    username = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix'}))

    def clean(self):
        username = self.cleaned_data.get('username')


#:::::affiliate-3:::::::::reg-web:::::::::
class RegWebForm(forms.Form):
    username = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix'}))
    email = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'email'}))
    password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password1'}))
    password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password2'}))



    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if len(username) < 1:
            raise forms.ValidationError("Enter username!")

        else:
            user_exist = UserProfile.objects.filter(username__iexact=username).exists()
            if user_exist:
                raise forms.ValidationError("Username already taken!")
            else:
                if len(email) < 1:
                    raise forms.ValidationError("Enter email address!")
                else:
                    email_correction = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
                    if email_correction == None:
                        raise forms.ValidationError("Email not correct!")
                    else:
                        email_exist = UserProfile.objects.filter(email__iexact=email).exists()
                        if email_exist:
                            raise forms.ValidationError("Email already exist!")
                        else:
                            if len(password1) < 8:
                                raise forms.ValidationError("Password is too short!")
                            else:
                                if password1 != password2:
                                    raise forms.ValidationError("Password not matched!")

    def registration(self, user_id=None):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')

        sponsor_obj = UserProfile.objects.get(username=user_id)

        user = UserProfile(username=username, email=email)
        user.set_password(password1)
        user.save()

        current_user = UserProfile.objects.get(id=user.id)

        UserProfile.addReferral(user_id, current_user)

        current_user_obj = UserProfile.objects.filter(id=user.id).update(sponsor=sponsor_obj)

        return user

#:::::::::::end reg-web::::::::::::::




#login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if len(username) < 1:
            raise forms.ValidationError("Enter Username!")
        else:
            if len(password) < 8:
                raise forms.ValidationError("Password is too short!")
            else:
                user = authenticate(username=username, password=password)
                if not user or not user.is_active:
                    raise forms.ValidationError("Username or Password not matched!")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


#user form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('email', 'phone_number', 'website', 'facebook', 'skype', 'profile_picture')


#basic info edit form
class BasicInfoEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'website', 'facebook', 'skype', 'profile_picture', )


#getresponse form
isEnabledChoice = (
    ('enable', 'Enable'),
    ('disable', 'Disable')
)
class GetResponseAutoresponderAddContactForm(forms.ModelForm):
    class Meta:
        model = models.GetResponseAutoresponderAddContact
        fields = ('campaignId', 'api_key', 'isEnable', )



#click magic account edit
class ClickMagicAccountEditForm(forms.ModelForm):
    class Meta:
        model = models.ClickMagicAccount
        fields = ('clickmagic_username', )


#click funnels account edit
class ClickFunnelsAccountEditForm(forms.ModelForm):
    class Meta:
        model = models.ClickFunnelsAccount
        fields = ('clickfunnels_username', )


#getresponse account edit
class GetResponseAccountEditForm(forms.ModelForm):
    class Meta:
        model = models.GetResponseAccount
        fields = ('getresponse_username', )


#aweber account edit
class AweberAccountEditForm(forms.ModelForm):
    class Meta:
        model = models.AweberAccount
        fields = ('aweber_username', )


#ledger nano s account edit
class LedgerNanoSEditForm(forms.ModelForm):
    class Meta:
        model = models.LedgerNanoSAccount
        fields = ('ledger_nano_s_username', )



#trezor s account edit
class TrezorSEditForm(forms.ModelForm):
    class Meta:
        model = models.TrezorSAccount
        fields = ('trezor_username', )


#coinbase account edit
class CoinBaseEditForm(forms.ModelForm):
    class Meta:
        model = models.CoinBaseAccount
        fields = ('coinbase_username', )


#spectrocoin card account edit
class SpectrocoinCardEditForm(forms.ModelForm):
    class Meta:
        model = models.SpectroCoinCardAccount
        fields = ('spectrocoin_card_username', )


#cryptopay card card account edit
class CryptoPayCardEditForm(forms.ModelForm):
    class Meta:
        model = models.CryptoPayCardAccount
        fields = ('cryptopay_card_username', )



#cex io account edit
class CexIOEditForm(forms.ModelForm):
    class Meta:
        model = models.CexIOAccount
        fields = ('cexio_username', )


#bit panda account edit
class BitPandaEditForm(forms.ModelForm):
    class Meta:
        model = models.BitPandaAccount
        fields = ('bitpanda_username', )



#local bitcoins account edit
class LocalBitcoinsEditForm(forms.ModelForm):
    class Meta:
        model = models.LocalBitcoinsAccount
        fields = ('local_bitcoins_username', )



#inda coin account edit
class IndaCoinEditForm(forms.ModelForm):
    class Meta:
        model = models.IndaCoinAccount
        fields = ('indacoin_username', )



#coin mama account edit
class CoinMamaEditForm(forms.ModelForm):
    class Meta:
        model = models.CoinMamaAccount
        fields = ('coin_mama_username', )



#ITB account edit
class ITBEditForm(forms.ModelForm):
    class Meta:
        model = models.ITBAccount
        fields = ('itb_username', )




#change password form
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    new_password1 = forms.CharField(label='New Password', max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    new_password2 = forms.CharField(label='Confirm Password', max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))

    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if len(new_password1) < 8:
            raise forms.ValidationError("Password is too short!")
        else:
            if new_password1 != new_password2:
                raise forms.ValidationError("Password not matched!")




#profile picture upload form
class ProfilePictureUploadForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = models.UserProfile
        fields = ('profile_picture', )

    def clean(self):
        photo = self.cleaned_data.get('profile_picture')

        if photo == None:
            raise forms.ValidationError('Select photo to upload!')



