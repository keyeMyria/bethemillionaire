from django import forms
import re

from django.contrib.auth.hashers import make_password, check_password

from account import models as account_model

from . import models

#video link form
lesson_list = (
    ('m_1_l_1', 'Module-1-Lesson-1'),
    ('m_1_l_2', 'Module-1-Lesson-2'),
    ('m_2_l_1', 'Module-2-Lesson-1'),
    ('m_2_l_2', 'Module-2-Lesson-2'),
    ('m_2_l_3', 'Module-2-Lesson-3'),
    ('m_2_l_4', 'Module-2-Lesson-4'),
    ('m_3_l_1', 'Module-3-Lesson-1'),
    ('m_3_l_2', 'Module-3-Lesson-2'),
    ('m_3_l_3', 'Module-3-Lesson-3'),
    ('m_4_l_1', 'Module-4-Lesson-1'),
    ('m_4_l_2', 'Module-4-Lesson-2'),
    ('m_4_l_3', 'Module-4-Lesson-3'),
    ('m_5_l_1', 'Module-5-Lesson-1'),
    ('m_5_l_2', 'Module-5-Lesson-2'),
    ('m_5_l_3', 'Module-5-Lesson-3'),
    ('m_5_l_4', 'Module-5-Lesson-4'),
    ('m_5_l_5', 'Module-5-Lesson-5'),
    ('m_5_l_6', 'Module-5-Lesson-6'),
    ('m_6_l_1', 'Module-6-Lesson-1'),
    ('m_6_l_2', 'Module-6-Lesson-2'),
    ('m_7_l_1', 'Module-7-Lesson-1'),
    ('m_7_l_2', 'Module-7-Lesson-2'),
    ('m_7_l_3', 'Module-7-Lesson-3'),
)

class VideoLinkForm(forms.Form):
    lesson_name = forms.ChoiceField(choices=lesson_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    video_link = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )


    def clean(self):
        lesson_name = self.cleaned_data.get('lesson_name')
        video_link = self.cleaned_data.get('video_link')


        if len(lesson_name) == 0:
            raise forms.ValidationError('Choose lesson name!')
        else:
            if len(video_link) == 0:
                raise forms.ValidationError('Enter the youtube video link!')



    def deploy(self):
        lesson_name = self.cleaned_data.get('lesson_name')
        video_link = self.cleaned_data.get('video_link')


        #deploy = models.VideoLink(lesson_name=lesson_name, video_link=video_link)
        #deploy.save()

        deploy = models.VideoLink.objects.update_or_create(lesson_name=lesson_name, defaults={'video_link': video_link})






#change user password from staff
class ChangeUserPasswordForm(forms.Form):
    new_password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    new_password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))

    def clean(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if len(new_password1) < 8:
            raise forms.ValidationError("Password is too short!")
        else:
            if new_password1 != new_password2:
                raise forms.ValidationError("Password not matched!")


    def deploy(self, user_id):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        hash_pass = make_password(new_password1)

        deploy = account_model.UserProfile.objects.filter(id=user_id).update(password=hash_pass)




#change membership
class ChangeMembershipForm(forms.ModelForm):
    membership = forms.ModelChoiceField(queryset=account_model.Membershiplevel.objects.all(), required=False,widget=forms.Select(attrs={'class':'input-field browser-default'}))

    class Meta:
        model = account_model.UserProfile
        fields = ('membership', )




#webinar registration form
class WebinarLinkForm(forms.ModelForm):
    class Meta:
        model = account_model.WebinarLink
        fields = ('link', )



#create leaderboard form
class CreateLeaderBoardForm(forms.Form):
    start_date = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))
    end_date = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))
    campaign_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        campaign_name = self.cleaned_data.get('campaign_name')


        if len(campaign_name) < 1:
            raise forms.ValidationError('Enter Campaign Name!')
        else:
            campaign_exists = models.LeaderBoard.objects.filter(campaign_name=campaign_name).exists()

            if campaign_exists:
                raise forms.ValidationError('Campaign name already taken. Try another name!')
            else:
                if len(start_date) < 1:
                    raise forms.ValidationError('Select start date!')
                else:
                    if len(end_date) < 1:
                        raise forms.ValidationError('Select end date')



    def deploy(self, results):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        campaign_name = self.cleaned_data.get('campaign_name')

        i = 1
        for result in results:
            deploy = models.LeaderBoard(user=result[0], start_date=start_date, end_date=end_date, campaign_name=campaign_name, rank=i, referral=result[2], referral_sale=result[1])
            deploy.save()

            i = i + 1




#user search form
class UserSearchForm(forms.Form):
    username = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'username'}))

    def clean(self):
        username = self.cleaned_data.get('username')


    def is_email(self, username):
        email_correction = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', username)

        if email_correction:
            return True
        else:
            return False


    def deploy(self):
        username = self.cleaned_data.get('username')

        is_email = self.is_email(username)

        if is_email:
            user = account_model.UserProfile.objects.filter(email=username)
        else:
            user = account_model.UserProfile.objects.filter(username=username)


        return user




#RecentUpdatePost
class RecentUpdatePostForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix'}))

    def clean(self):
        title = self.cleaned_data.get('title')


        if len(title) < 5:
            raise forms.ValidationError('Enter post title! Not less than 5 words!')


    def deploy(self, request, post):
        title = self.cleaned_data.get('title')

        deploy = models.RecentUpdatePost(user=request.user, title=title, post=post)
        deploy.save()





#edit recent update post
class RecentUpdatePostEditForm(forms.ModelForm):

    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix'}))
    post = forms.CharField( required=False, max_length= 5000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )


    class Meta:
        model = models.RecentUpdatePost
        fields = ('title', 'post')




#update live video link
class LiveVideoLinkUpdateForm(forms.Form):
    link = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )


    def clean(self):
        link = self.cleaned_data.get('link')

        if len(link) < 10:
            raise forms.ValidationError('Insert valid link!')



    def deploy(self, request):
        link = self.cleaned_data.get('link')

        deploy = models.LiveVideoLinkUpdate(link=link, user=request.user)
        deploy.save()





