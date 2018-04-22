from django import forms
from django.db.models import Q

from . import models


#team create form
class TeamForm(forms.Form):
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop('request')
        super(TeamForm, self).__init__(*args,**kwargs)

    name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))

    def clean(self):
        name = self.cleaned_data.get('name')

        if len(name) == 0:
            raise forms.ValidationError('Enter team name!')
        else:
            check_unique_name = models.Team.objects.filter(Q(owner=self.request.user) & Q(name=name)).exists()
            if check_unique_name:
                raise forms.ValidationError('This team name is already exists, try another!')

    def deploy(self):
        name = self.cleaned_data.get('name')

        deploy = models.Team(owner=self.request.user, name=name)
        deploy.save()



#personal training content upload form
class PersonalTrainingContentForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    description = forms.CharField( required=False, max_length= 5000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    video = forms.FileField(required=False)

    def clean(self):
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        video = self.cleaned_data.get('video')


        if len(title) == 0:
            raise forms.ValidationError('Enter title!')
        else:
            if len(description) == 0:
                raise forms.ValidationError('Enter description!')



    def deploy(self, owner, team):
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        video = self.cleaned_data.get('video')


        deploy = models.PersonalTrainingContent(owner=owner, team=team, title=title, description=description, video=video)
        deploy.save()






#payment account setting form
account_type_list = (
    ('bitcoin', 'Bitcoin'),
    ('paypal', 'Paypal'),
)
class PaymentAccountSettingForm(forms.Form):
    account_type = forms.ChoiceField(choices=account_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    account_no = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix'}))


    def clean(self):
        account_type = self.cleaned_data.get('account_type')
        account_no = self.cleaned_data.get('account_no')

        if len(account_no) == 0:
            raise forms.ValidationError('Enter the account no!')



    def deploy(self, request):
        account_type = self.cleaned_data.get('account_type')
        account_no = self.cleaned_data.get('account_no')


        deploy = models.PaymentAccountSetting.objects.update_or_create(user=request.user, defaults={'account_type': account_type, 'account_no': account_no})



