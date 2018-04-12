from django import forms

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


