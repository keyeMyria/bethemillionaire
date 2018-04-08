from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),

    #affiliate link
    url(r'^member-home/affiliate-link/$', views.AffiliateLink.as_view(), name='affiliate_link'),
    url(r'^member-home/email-swipes/$', views.EmailSwipes.as_view(), name='email_swipes'),
    url(r'^member-home/banners/$', views.Banners.as_view(), name='banners'),

    #dashboard - bitcoin basics links
    url(r'^member-home/what-is-bitcoin/$', views.WhatIsBitcoin.as_view(), name='what-is-bitcoin'),
    url(r'^member-home/buy-bitcoins-here/$', views.BuyBitcoinHere.as_view(), name='buy-bitcoins-here'),
    url(r'^member-home/bitcoin-wallets/$', views.BitcoinWallet.as_view(), name='bitcoin-wallets'),
    url(r'^member-home/bitcoin-debit-cards/$', views.BitcoinDebitCard.as_view(), name='bitcoin-debit-cards'),

    #privacy policy
    url(r'^member-home/privacy-policy/$', views.PrivacyPolicy.as_view(), name='privacy-policy'),
    url(r'^member-home/faq/$', views.FAQ.as_view(), name='faq'),
    url(r'^member-home/recent-update/$', views.RecentUpdate.as_view(), name='recent-update'),
]
