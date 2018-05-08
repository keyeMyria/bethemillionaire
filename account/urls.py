from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name='login'),

    #1st 2 affiliate link
    url(r'^pre-registration/$', views.Preregistration.as_view(), name='preregistration'),
    url(r'^registration/$', views.Registration.as_view(), name='registration'),

    #3rd affiliate link
    url(r'^pre-web/$', views.PreWeb.as_view(), name='pre-web'),
    url(r'^reg-web/$', views.RegWeb.as_view(), name='reg-web'),
    url(r'^web-confirmation/$', views.WebConfirmation.as_view(), name='web-confirmation'),

    #4th affiliate link
    url(r'^webinar/$', views.Webinar.as_view(), name='webinar'),
    url(r'^live-web-class/$', views.LiveWebClass.as_view(), name='live-web-class'),
    url(r'^watchlivewebclass/$', views.WatchLiveWebClass.as_view(), name='watchlivewebclass'),

    #5th affiliate link
    url(r'^get-your-course/$', views.GetYourCourse.as_view(), name='get-your-course'),

    #6th affiliate link
    url(r'^secrets-to-wealth/$', views.SecretsToWealth.as_view(), name='secrets-to-wealth'),
    url(r'^secrets-to-wealth-final/$', views.SecretsToWealthFinal.as_view(), name='secrets-to-wealth-final'),

    #7th affiliate link
    url(r'^webinar-replay/$', views.WebinarReplay.as_view(), name='webinar-replay'),

    #8th affiliate link
    url(r'^pre-usi/$', views.PreUsi.as_view(), name='pre-usi'),
    url(r'^reg-usi/$', views.RegUsi.as_view(), name='reg-usi'),
    url(r'^usi-2/$', views.Usi2.as_view(), name='usi-2'),
    url(r'^usi-tech-fast-start/$', views.UsiTechFastStart.as_view(), name='usi-tech-fast-start'),

    #9th affiliate link
    url(r'^usi/$', views.Usi.as_view(), name='usi'),

    #11th affiliate link
    url(r'^bitconnect/$', views.Bitconnect.as_view(), name='bitconnect'),
    url(r'^bcc-fast-start/$', views.BccFastStart.as_view(), name='bcc-fast-start'),

    #12th affiliate link
    url(r'^7-figure-strategies/$', views.SevenFigureStrategies.as_view(), name='7-figure-strategies'),

    #13th affiliate link
    url(r'^how-to-set-up-your-btm-system/$', views.HowToSetUpYourBTMSystem.as_view(), name='how-to-set-up-your-btm-system'),

    #14th affiliate link
    url(r'^7-figure-plan/$', views.SevenFigurePlan.as_view(), name='7-figure-plan'),

    url(r'^access/$', views.Access.as_view(), name='access'),
    url(r'^logout/$', views.logout_request, name='logout'),

    url(r'^membership-account/profile/$', views.Profile.as_view(), name='profile'),
    url(r'^membership-account/affiliate-network/$', views.AffiliateNetwork.as_view(), name='affiliate-network'),
    url(r'^membership-account/my-membership/$', views.MyMembership.as_view(), name='my-membership'),


    url(r'^membership-account/my-referrals/$', views.MyReferrals.as_view(), name='my-referrals'),
    url(r'^membership-account/public-profile/$', views.PublicProfile.as_view(), name='public-profile'),
    url(r'^membership-account/my-autoresponder-settings/$', views.MyAutoresponderSettings.as_view(), name='my-autoresponder-settings'),

    #upgrade membership
    url(r'^membership-account/premium-members/$', views.MembershipLevelPremium.as_view(), name='membership-level-premium'),
    url(r'^membership-account/vip-members/$', views.MembershipLevelVIP.as_view(), name='membership-level-vip'),
    url(r'^membership-account/membership-checkout/$', views.MembershipCheckout.as_view(), name='membership-checkout'),
    url(r'^membership-account/checkout-success/$', views.CheckoutSuccess.as_view(), name='checkout-success'),
    url(r'^membership-account/checkout-failure/$', views.CheckoutFailure.as_view(), name='checkout-failure'),


    #welcome video for direct registration
    url(r'^welcome/$', views.Welcome.as_view(), name='welcome'),
    url(r'^thank-you/$', views.ThankYou.as_view(), name='thank-you'),


    #paypal ipn
    url(r'^paypal-ipn/$', views.PaypalIPN, name='paypal-ipn'),



    url(r'^api/check-username/$', views.check_username, name='chech-username'),
    url(r'^api/user-profile/$', views.UserProfileAPI.as_view(), name='user-profile-api'),
    url(r'^api/affiliate-link/$', views.AffiliateLinkAPI.as_view(), name='affiliate-link-api'),
    url(r'^api/payment/$', views.PaymentAPI.as_view(), name='payment-api'),

]
