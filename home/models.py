from django.db import models

from account import models as account_model

class AffiliateLinkControl(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    short_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_name



#create team
class Team(models.Model):
    owner = models.ForeignKey(account_model.UserProfile, related_name='team_owner', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    member = models.ManyToManyField(account_model.UserProfile, related_name='team_member', blank=True)
    creation_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.owner.username) + '-' + str(self.name)


    @classmethod
    def addMember(cls, users, team_id, newMember):
        referral, created = cls.objects.get_or_create(
            owner = users,
            id=team_id
        )

        referral.member.add(newMember)


    @classmethod
    def removeMember(cls, users, team_id, newMember):
        referral, created = cls.objects.get_or_create(
            owner = users,
            id=team_id
        )
        referral.member.remove(newMember)




#personal training file upload
class PersonalTrainingContent(models.Model):
    owner =  models.ForeignKey(account_model.UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)

    video = models.FileField(upload_to='personal_training/video/', null=True, blank=True)

    creation_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.owner.username) + ":" + str(self.team.name)


    class Meta:
        ordering = ('-creation_time', )



#commission payment receiver account
class PaymentAccountSetting(models.Model):
    user = models.OneToOneField(account_model.UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    account_type = models.CharField(max_length=50, null=True, blank=True)
    account_no = models.CharField(max_length=255, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)




#live chat message
class LiveChatMessage(models.Model):
    room = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(account_model.UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.id)



