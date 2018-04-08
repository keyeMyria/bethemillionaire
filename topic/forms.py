from django import forms
from django.contrib.auth.models import User

from topic import models
from account.models import UserProfile
from account.models import UsiTechAccount, BitconnectAccount

class CommentForm(forms.Form):
    comment = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea', 'id': 'icon_prefix'}) )

    def clean(self):
        comment = self.cleaned_data.get('comment')

    def deploy(self, request):
        comment = self.cleaned_data.get('comment')
        user = request.user.username

        user_profile = UserProfile.objects.get(username=user)

        deploy = models.Comment(user=user_profile, comment=comment)

        return deploy


class SubCommentForm(forms.Form):
    subcomment = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea', 'id': 'icon_prefix'}) )

    def clean(self):
        subcomment = self.cleaned_data.get('subcomment')

    def deploy(self, request, comment_id=None):
        subcomment = self.cleaned_data.get('subcomment')
        user = request.user.username

        user_profile = UserProfile.objects.get(username=user)
        comment_obj = models.Comment.objects.get(id=comment_id)

        deploy = models.SubComment(user=user_profile, comment=comment_obj, subcomment=subcomment)

        return deploy


#usi-tech account username  store
class UsiTechAccountForm(forms.ModelForm):
    usi_username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix'}))

    class Meta:
        model = UsiTechAccount
        fields = ('usi_username', )

    def clean(self):
        usi_username = self.cleaned_data.get('usi_username')

    def deploy(self, request):
        usi_username = self.cleaned_data.get('usi_username')

        username = request.user.username
        user_obj = UserProfile.objects.get(username=username)

        deploy = UsiTechAccount.objects.filter(user=user_obj).update(usi_username=usi_username)


#bitconnect account username  store
class BitconnectAccountForm(forms.ModelForm):
    bitconnect_username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix'}))

    class Meta:
        model = BitconnectAccount
        fields = ('bitconnect_username', )

    def clean(self):
        bitconnect_username = self.cleaned_data.get('bitconnect_username')

    def deploy(self, request):
        bitconnect_username = self.cleaned_data.get('bitconnect_username')

        username = request.user.username
        user_obj = UserProfile.objects.get(username=username)

        deploy = BitconnectAccount.objects.filter(user=user_obj).update(bitconnect_username=bitconnect_username)


class NoteForm(forms.ModelForm):
    note = forms.CharField(required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea', 'id': 'icon_prefix'}) )

    class Meta:
        model = models.Note
        fields = ('note', )

    def clean(self):
        note = self.cleaned_data.get('note')

    def deploy(self, request, topic):
        note = self.cleaned_data.get('note')
        user = request.user

        defaults = {'note': note}

        obj, created = models.Note.objects.update_or_create(user=user, topic=topic, defaults=defaults)
