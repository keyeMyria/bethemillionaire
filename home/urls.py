from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),

    #affiliate link
    url(r'^member-home/affiliate-link/$', views.AffiliateLink.as_view(), name='affiliate_link'),
    url(r'^member-home/email-swipes/$', views.EmailSwipes.as_view(), name='email_swipes'),
    url(r'^member-home/banners/$', views.Banners.as_view(), name='banners'),

    #passive profits
    url(r'^member-home/passive-income/$', views.PassiveIncome.as_view(), name='passive-income'),

    #payment settings
    url(r'^member-home/payment-account-setting/$', views.PaymentAccountSetting.as_view(), name='payment-account-setting'),

    #my commission
    url(r'^member-home/my-commission/$', views.MyCommission.as_view(), name='my-commission'),

    #leader board
    url(r'^member-home/leader-board/$', views.LeaderBoard.as_view(), name='leader-board'),


    #training by sponsor
    url(r'^member-home/manage-team/$', views.ManageTeam.as_view(), name='manage-team'),
    url(r'^member-home/add-team-member/$', views.AddTeamMemberOperation.as_view(), name='add-team-member'),
    url(r'^member-home/remove-team-member/$', views.RemoveTeamMemberOperation.as_view(), name='remove-team-member'),

    url(r'^member-home/training/(?P<owner_id>[0-9]+)/(?P<team_id>[0-9]+)/$', views.PersonalTraining.as_view(), name='personal-training'),

    #dashboard - bitcoin basics links
    url(r'^member-home/what-is-bitcoin/$', views.WhatIsBitcoin.as_view(), name='what-is-bitcoin'),
    url(r'^member-home/buy-bitcoins-here/$', views.BuyBitcoinHere.as_view(), name='buy-bitcoins-here'),
    url(r'^member-home/bitcoin-wallets/$', views.BitcoinWallet.as_view(), name='bitcoin-wallets'),
    url(r'^member-home/bitcoin-debit-cards/$', views.BitcoinDebitCard.as_view(), name='bitcoin-debit-cards'),

    #privacy policy
    url(r'^member-home/privacy-policy/$', views.PrivacyPolicy.as_view(), name='privacy-policy'),
    url(r'^member-home/faq/$', views.FAQ.as_view(), name='faq'),
    url(r'^member-home/recent-update/$', views.RecentUpdate.as_view(), name='recent-update'),

    url(r'^start/$', views.Start.as_view(), name='start'),
]
