from rest_framework import serializers
from . import models
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    sponsor_username = serializers.CharField(source='sponsor.username')
    sponsor_email = serializers.CharField(source='sponsor.email')
    sponsor_phone = serializers.CharField(source='sponsor.phone_number')
    sponsor_skype = serializers.CharField(source='sponsor.skype')
    sponsor_profile_picture = serializers.CharField(source='sponsor.profile_picture')

    class Meta:
        model = UserProfile
        exclude = ('password', 'last_login', 'is_superuser', 'join_date', 'is_active', 'is_staff', 'membership', 'sponsor', 'groups', 'user_permissions', 'referrals')
        #fields = '__all__'


##------------------------------
##------------------------------
##serializer for refer programme
##14 model serializer-----------
##------------------------------
##------------------------------


#serializer 1
class BeTheMillionaire_3_Step_Registration_Funnel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.BeTheMillionaire_3_Step_Registration_Funnel
        fields = '__all__'


#serializer 2
class Direct_Registration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Direct_Registration
        fields = '__all__'


#serializer 3
class Automated_Webinar_Funnel_Version_1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Automated_Webinar_Funnel_Version_1
        fields = '__all__'


#serializer 4
class Automated_Webinar_Funnel_Version_2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Automated_Webinar_Funnel_Version_2
        fields = '__all__'


#serializer 5
class Course_Giveaway_Direct_Registration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course_Giveaway_Direct_Registration
        fields = '__all__'


#serializer 6
class Course_Giveaway_3_Steps_Funnel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course_Giveaway_3_Steps_Funnel
        fields = '__all__'


#serializer 7
class Latest_Webinar_Replay_BTM_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Latest_Webinar_Replay_BTM
        fields = '__all__'


#serializer 8
class Usi_Tech_Funnel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usi_Tech_Funnel
        fields = '__all__'


#serializer 9
class Usi_Tech_Direct_Funnel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usi_Tech_Direct_Funnel
        fields = '__all__'


#serializer 10
class Usi_Tech_Btc_Packages_Calculator_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usi_Tech_Btc_Packages_Calculator
        fields = '__all__'


#serializer 11
class Bitconnect_Direct_Funnel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bitconnect_Direct_Funnel
        fields = '__all__'


#serializer 12
class Mike_Hobbs_Usi_Tech_Team_Webinar_90_bitcoins_in_6_months_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mike_Hobbs_Usi_Tech_Team_Webinar_90_bitcoins_in_6_months
        fields = '__all__'


#serializer 13
class How_To_Set_Up_Your_BeTheMillionaire_System_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.How_To_Set_Up_Your_BeTheMillionaire_System
        fields = '__all__'


#serializer 14
class Usi_Tech_7_Figure_Plan_In_2018_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usi_Tech_7_Figure_Plan_In_2018
        fields = '__all__'


#payment serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        exclude = ('creation_time',)
