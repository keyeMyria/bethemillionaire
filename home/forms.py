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


