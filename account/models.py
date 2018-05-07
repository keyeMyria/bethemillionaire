from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class Preregistration(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.email


# user profile manager
class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model"""

    def create_user(self, username, email, membership=None, sponsor=None, phone_number=None, website=None, facebook=None, skype=None, profile_picture=None, join_date=None, password=None):
        """creates a new user profile objecs"""

        if not email:
            raise ValueError('User must have an email address!')

        if not username:
            raise ValueError('User must have an username!')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, membership=membership, sponsor=sponsor, phone_number=phone_number, website=website, facebook=facebook, skype=skype, profile_picture=profile_picture, join_date=join_date)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, username, email, password):
        """creates and saves a new super user with given details"""

        user = self.create_user(username=username, email=email, password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



# user profile model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside our system"""

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    membership = models.ForeignKey('Membershiplevel', related_name='membership_level', default=1, null=True, blank=True)

    payments = models.ForeignKey('Payment', null=True, blank=True, related_name='last_payments' )

    sponsor = models.ForeignKey('UserProfile', related_name='sponsors', null=True, blank=True)
    referrals = models.ManyToManyField('UserProfile', related_name='referral', blank=True)
    phone_number = models.CharField(max_length=18, null=True, blank=True)
    website = models.CharField(max_length=400, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    skype = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/user/', null=True, blank=True)


    join_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]


    def get_full_name(self):
        """Used to get a users full name."""

        return self.username

    def get_short_name(self):
        """Used to get a users short name."""

        return self.username

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.username

    @classmethod
    def addReferral(cls, users, newReferral):
        referral, created = cls.objects.get_or_create(
            username = users
        )

        referral.referrals.add(newReferral)


    @classmethod
    def removeReferral(cls, users, newReferral):
        referral, created = cls.objects.get_or_create(
            username = users
        )
        referral.referrals.remove(newReferral)



"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, related_name='users')
    membership = models.ForeignKey('Membershiplevel', default=1, related_name='membership_level')
    sponsor = models.ForeignKey('UserProfile', default=1, related_name='sponsors', null=True, blank=True)
    referrals = models.ManyToManyField(User, related_name='referral')
    phone_number = models.CharField(max_length=18, null=True, blank=True)
    website = models.CharField(max_length=400, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    skype = models.CharField(max_length=100, null=True, blank=True)
    my_reffer_id = models.SlugField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/user/', null=True, blank=True)


    def __str__(self):
        return str(self.user.username)


    @classmethod
    def addReferral(cls, users, newReferral):
        referral, created = cls.objects.get_or_create(
            user = users
        )

        referral.referrals.add(newReferral)


    @classmethod
    def removeReferral(cls, users, newReferral):
        referral, created = cls.objects.get_or_create(
            user = users
        )
        referral.referrals.remove(newReferral)


    def _get_unique_slug(self):
        my_reffer_id = slugify(self.user.username)
        unique_refer_id = my_reffer_id
        num = 1
        while UserProfile.objects.filter(my_reffer_id=unique_refer_id).exists():
            unique_refer_id = '{}-{}'.format(my_reffer_id, num)
            num += 1
        return unique_refer_id

    def save(self, *args, **kwargs):
        if not self.my_reffer_id:
            self.my_reffer_id = self._get_unique_slug()
        super().save()


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
"""


##--------------------------##
##--------------------------##
##Refer programme database--##
##14 table                  ##
##--------------------------##
##--------------------------##


#table 1
class BeTheMillionaire_3_Step_Registration_Funnel(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user1')
    campaign_name = models.CharField(max_length=100, default='BeTheMillionaire 3-Step Registration Funnel', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)


def create_affiliate1(sender, **kwargs):
    if kwargs['created']:
        affiliate1 = BeTheMillionaire_3_Step_Registration_Funnel.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate1, sender=UserProfile)


#table 2
class Direct_Registration(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user2')
    campaign_name = models.CharField(max_length=100, default='Direct Registration', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)


def create_affiliate2(sender, **kwargs):
    if kwargs['created']:
        affiliate2 = Direct_Registration.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate2, sender=UserProfile)


#table 3
class Automated_Webinar_Funnel_Version_1(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user3')
    campaign_name = models.CharField(max_length=100, default='Automated Webinar Funnel Version 1', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)


def create_affiliate3(sender, **kwargs):
    if kwargs['created']:
        affiliate3 = Automated_Webinar_Funnel_Version_1.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate3, sender=UserProfile)


#table 4
class Automated_Webinar_Funnel_Version_2(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user4')
    campaign_name = models.CharField(max_length=100, default='Automated Webinar Funnel Version 2', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)


def create_affiliate4(sender, **kwargs):
    if kwargs['created']:
        affiliate4 = Automated_Webinar_Funnel_Version_2.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate4, sender=UserProfile)


#table 5
class Course_Giveaway_Direct_Registration(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user5')
    campaign_name = models.CharField(max_length=100, default='Course Giveaway Direct Registration', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)

def create_affiliate5(sender, **kwargs):
    if kwargs['created']:
        affiliate5 = Course_Giveaway_Direct_Registration.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate5, sender=UserProfile)


#table 6
class Course_Giveaway_3_Steps_Funnel(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user6')
    campaign_name = models.CharField(max_length=100, default='Course Giveaway 3 Steps Funnel', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)

def create_affiliate6(sender, **kwargs):
    if kwargs['created']:
        affiliate6 = Course_Giveaway_3_Steps_Funnel.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate6, sender=UserProfile)


#table 7
class Latest_Webinar_Replay_BTM(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user7')
    campaign_name = models.CharField(max_length=100, default='Latest Webinar Replay BTM', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)

def create_affiliate7(sender, **kwargs):
    if kwargs['created']:
        affiliate7 = Latest_Webinar_Replay_BTM.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate7, sender=UserProfile)


#table 8
class Usi_Tech_Funnel(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user8')
    campaign_name = models.CharField(max_length=100, default='Usi-Tech Funnel', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)


def create_affiliate8(sender, **kwargs):
    if kwargs['created']:
        affiliate8 = Usi_Tech_Funnel.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate8, sender=UserProfile)


#table 9
class Usi_Tech_Direct_Funnel(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user9')
    campaign_name = models.CharField(max_length=100, default='Usi-Tech Direct Funnel', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)

def create_affiliate9(sender, **kwargs):
    if kwargs['created']:
        affiliate9 = Usi_Tech_Direct_Funnel.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate9, sender=UserProfile)


#table 10
class Usi_Tech_Btc_Packages_Calculator(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user10')
    campaign_name = models.CharField(max_length=100, default='USI-TECH BTC-Packages Calculator', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')


    def __str__(self):
        return str(self.user.username)

def create_affiliate10(sender, **kwargs):
    if kwargs['created']:
        affiliate10 = Usi_Tech_Btc_Packages_Calculator.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate10, sender=UserProfile)


#table 11
class Bitconnect_Direct_Funnel(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user11')
    campaign_name = models.CharField(max_length=100, default='Bitconnect Direct Funnel', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)

def create_affiliate11(sender, **kwargs):
    if kwargs['created']:
        affiliate11 = Bitconnect_Direct_Funnel.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate11, sender=UserProfile)


#table 12
class Mike_Hobbs_Usi_Tech_Team_Webinar_90_bitcoins_in_6_months(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user12')
    campaign_name = models.CharField(max_length=100, default='Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)

def create_affiliate12(sender, **kwargs):
    if kwargs['created']:
        affiliate12 = Mike_Hobbs_Usi_Tech_Team_Webinar_90_bitcoins_in_6_months.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate12, sender=UserProfile)


#table 13
class How_To_Set_Up_Your_BeTheMillionaire_System(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user13')
    campaign_name = models.CharField(max_length=100, default='How To Set Up Your BeTheMillionaire System', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)
    campaign_link = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return str(self.user.username)

def create_affiliate13(sender, **kwargs):
    if kwargs['created']:
        affiliate13 = How_To_Set_Up_Your_BeTheMillionaire_System.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate13, sender=UserProfile)


#table 14
class Usi_Tech_7_Figure_Plan_In_2018(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True, related_name='user14')
    campaign_name = models.CharField(max_length=100, default='Usi Tech 7 Figure Plan In 2018!', null=True)
    visitors = models.IntegerField(null=True, blank=True, default=0)
    leads = models.IntegerField(null=True, blank=True, default=0)
    conversion_rate = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.user.username)

def create_affiliate14(sender, **kwargs):
    if kwargs['created']:
        affiliate14 = Usi_Tech_7_Figure_Plan_In_2018.objects.create(user=kwargs['instance'])

post_save.connect(create_affiliate14, sender=UserProfile)



#autoresponder setup
#getresponse autoresponder add contacts db
class GetResponseAutoresponderAddContact(models.Model):
    user = models.OneToOneField(UserProfile, null=True, blank=True)
    campaignId = models.CharField(max_length=30, default='', null=True, blank=True)
    api_key = models.CharField(max_length=50, default='', null=True, blank=True)
    isEnable = models.CharField(max_length=10, default='enable', null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


def create_getresponseaddcontact(sender, **kwargs):
    if kwargs['created']:
        getresponseaddcontact = GetResponseAutoresponderAddContact.objects.create(user=kwargs['instance'])

post_save.connect(create_getresponseaddcontact, sender=UserProfile)


#membership levels
class Membershiplevel(models.Model):
    level = models.IntegerField(default=1, null=True, blank=True)
    name = models.CharField(max_length=50, default='free', null=True, blank=True)
    package = models.CharField(max_length=20, default='free', null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name + "-" + self.package



#paypal ipn data
class PaypalConfirmation(models.Model):
    transaction_ID = models.CharField(max_length=100, null=True, blank=True)
    ipn_message = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return str(self.transaction_ID)



#payment
class Payment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=None, null=True, blank=True)
    intent = models.CharField(max_length=50, null=True, blank=True)
    payer_ID = models.CharField(max_length=100, null=True, blank=True)
    payment_ID = models.CharField(max_length=100, null=True, blank=True)
    payment_Token = models.CharField(max_length=100, null=True, blank=True)
    transaction_ID = models.CharField(max_length=100, null=True, blank=True)

    paypal_confirmation = models.ForeignKey(PaypalConfirmation, on_delete=None, null=True, blank=True)

    membership = models.ForeignKey(Membershiplevel, null=True, blank=True)

    #this is for manual verification protect fraud transaction
    is_verify = models.CharField(max_length=10, default='pending')
    creation_time = models.DateTimeField(auto_now_add=True)
    expired_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


#usi tech account
class UsiTechAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    usi_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_UsiTechAccount(sender, **kwargs):
    if kwargs['created']:
        usitechaccount = UsiTechAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_UsiTechAccount, sender=UserProfile)


#bitconnect account
class BitconnectAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    bitconnect_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_BitconnectAccount(sender, **kwargs):
    if kwargs['created']:
        bitconnectaccount = BitconnectAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_BitconnectAccount, sender=UserProfile)


#click magic account
class ClickMagicAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    clickmagic_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

def create_ClickMagicAccount(sender, **kwargs):
    if kwargs['created']:
        clickmagicaccount = ClickMagicAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_ClickMagicAccount, sender=UserProfile)


#click funnels account
class ClickFunnelsAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    clickfunnels_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

def create_ClickFunnelsAccount(sender, **kwargs):
    if kwargs['created']:
        clickfunnelsaccount = ClickFunnelsAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_ClickFunnelsAccount, sender=UserProfile)



#getresponse account
class GetResponseAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    getresponse_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

def create_GetResponseAccount(sender, **kwargs):
    if kwargs['created']:
        getresponseaccount = GetResponseAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_GetResponseAccount, sender=UserProfile)


#aweber account
class AweberAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    aweber_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

def create_AweberAccount(sender, **kwargs):
    if kwargs['created']:
        aweberaccount = AweberAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_AweberAccount, sender=UserProfile)



#ledger nano s account
class LedgerNanoSAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    ledger_nano_s_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

def create_LedgerNanoSAccount(sender, **kwargs):
    if kwargs['created']:
        ledger_nano_s = LedgerNanoSAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_LedgerNanoSAccount, sender=UserProfile)



#trezor account
class TrezorSAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    trezor_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_TrezorSAccount(sender, **kwargs):
    if kwargs['created']:
        trezor_s = TrezorSAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_TrezorSAccount, sender=UserProfile)




#coin base account
class CoinBaseAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    coinbase_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_CoinBaseAccount(sender, **kwargs):
    if kwargs['created']:
        coinbase = CoinBaseAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_CoinBaseAccount, sender=UserProfile)



#spectrocoin card account
class SpectroCoinCardAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    spectrocoin_card_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

def create_SpectroCoinCardAccount(sender, **kwargs):
    if kwargs['created']:
        spectrocoin_card = SpectroCoinCardAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_SpectroCoinCardAccount, sender=UserProfile)




#cryptopay card account
class CryptoPayCardAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    cryptopay_card_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_CryptoPayCardAccount(sender, **kwargs):
    if kwargs['created']:
        cryptopay_card = CryptoPayCardAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_CryptoPayCardAccount, sender=UserProfile)



#cex.io account
class CexIOAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    cexio_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_CexIOAccount(sender, **kwargs):
    if kwargs['created']:
        cex_io = CexIOAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_CexIOAccount, sender=UserProfile)



#bitpanda account
class BitPandaAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    bitpanda_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_BitPandaAccount(sender, **kwargs):
    if kwargs['created']:
        bit_panda = BitPandaAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_BitPandaAccount, sender=UserProfile)



#local bitcoins account
class LocalBitcoinsAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    local_bitcoins_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_LocalBitcoinsAccount(sender, **kwargs):
    if kwargs['created']:
        local_bitcoins = LocalBitcoinsAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_LocalBitcoinsAccount, sender=UserProfile)



#indacoin account
class IndaCoinAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    indacoin_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_IndaCoinAccount(sender, **kwargs):
    if kwargs['created']:
        inda_coin = IndaCoinAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_IndaCoinAccount, sender=UserProfile)



#coin mama account
class CoinMamaAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    coin_mama_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)



def create_CoinMamaAccount(sender, **kwargs):
    if kwargs['created']:
        coin_mama = CoinMamaAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_CoinMamaAccount, sender=UserProfile)




#itb account
class ITBAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    itb_username = models.CharField(max_length=100, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)



def create_ITBAccount(sender, **kwargs):
    if kwargs['created']:
        itb = ITBAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_ITBAccount, sender=UserProfile)



#referral sale comission
class ReferralSaleCommission(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=None, null=True, blank=True, related_name='sponsor_comission')
    referred_user = models.ForeignKey(UserProfile, on_delete=None, null=True, blank=True, related_name='referred_user')
    referred_user_payment = models.ForeignKey(Payment, on_delete=None, null=True, blank=True)
    commission = models.FloatField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(UserProfile, on_delete=None, null=True, blank=True, related_name='verified_by_staff')
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)




#webinar link
class WebinarLink(models.Model):
    link = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.id)
