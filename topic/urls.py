from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^step-1-overview/$', views.Step_1.as_view(), name='step_1'),
    url(r'^step-2-set-up-your-bitcoin-wallet-load-it-with-bitcoins/$', views.Step_2.as_view(), name='step_2'),
    url(r'^step-3-wealth-vehicles/$', views.Step_3.as_view(), name='step_3'),
    url(r'^step-4-live-mentoring/$', views.Step_4.as_view(), name='step_4'),
    url(r'^step-5-start-promoting-bitcoins-wealth-club-system-earn-bitcoins-in-multiple-ways/$', views.Step_5.as_view(), name='step_5'),

    #url for module - 1
    url(r'^welcome-to-bethemillionaire-system/$', views.Lesson1.as_view(), name='module-1-lesson-1'),
    url(r'^overview/$', views.Lesson2.as_view(), name='module-1-lesson-2'),

    #url for module - 2
    url(r'^lesson-1-why-bitcoins/$', views.Module_2_Lesson_1.as_view(), name='module-2-lesson-1'),
    url(r'^lesson-2-best-bitcoin-wallets-to-use/$', views.Module_2_Lesson_2.as_view(), name='module-2-lesson-2'),
    url(r'^lesson-3-the-complete-guide-to-easily-buying-bitcoins-online-offline/$', views.Module_2_Lesson_3.as_view(), name='module-2-lesson-3'),
    url(r'^lesson-4-bitcoin-debit-cards/$', views.Module_2_Lesson_4.as_view(), name='module-2-lesson-4'),

    #url for module - 3
    url(r'^4-ways-to-produce-income/$', views.Module_3_Lesson_1.as_view(), name='module-3-lesson-1'),
    url(r'^lesson-2-why-banks-biggest-scammers/$', views.Module_3_Lesson_2.as_view(), name='module-3-lesson-2'),
    url(r'^5-primary-ways-to-grow-your-wealth-in-bitcoins/$', views.Module_3_Lesson_3.as_view(), name='module-3-lesson-3'),

    #url for module - 4
    url(r'^lesson-1-472-per-year-roi/$', views.Module_4_Lesson_1.as_view(), name='module-4-lesson-1'),
    url(r'^lesson-2-how-to-earn-multiple-streams-of-income-diversify-your-bitcoin-investments/$', views.Module_4_Lesson_2.as_view(), name='module-4-lesson-2'),
    url(r'^lesson-3-how-to-learn-from-multi-millionaires-like-kevin-harrington/$', views.Module_4_Lesson_3.as_view(), name='module-4-lesson-3'),

    #url for module - 5
    url(r'^lesson-1-set-up-bitcoins-wealth-club-system-correctly/$', views.Module_5_Lesson_1.as_view(), name='module-5-lesson-1'),
    url(r'^lesson-2-connect-your-autoresponder-to-bitcoins-wealth-club-to-build-your-list-optional/$', views.Module_5_Lesson_2.as_view(), name='module-5-lesson-2'),
    url(r'^lesson-3-how-to-promote-your-affiliate-links-funnels/$', views.Module_5_Lesson_3.as_view(), name='module-5-lesson-3'),
    url(r'^lesson-4-how-to-promote-bitcoins-wealth-club-on-facebook-groups/$', views.Module_5_Lesson_4.as_view(), name='module-5-lesson-4'),
    url(r'^lesson-5-how-to-learn-advanced-marketing-strategies-become-online-recruiting-master/$', views.Module_5_Lesson_5.as_view(), name='module-5-lesson-5'),
    url(r'^lesson-6-how-to-get-premium-vip-level-coaching-own-20-of-profits-of-bitcoins-wealth-club/$', views.Module_5_Lesson_6.as_view(), name='module-5-lesson-6'),

    #url for module - 6
    url(r'^lesson-1-how-to-leverage-micro-profit-system-to-trade-at-minimum-1-a-day/$', views.Module_6_Lesson_1.as_view(), name='module-6-lesson-1'),
    url(r'^how-my-friend-caleb-earns-over-1000000-a-year-trading-cryptocurrencies/$', views.Module_6_Lesson_2.as_view(), name='module-6-lesson-2'),

    #url for module - 7
    url(r'^how-to-achieve-your-goals-dreams/$', views.Module_7_Lesson_1.as_view(), name='module-7-lesson-1'),
    url(r'^lesson2-your-daily-method-of-operation/$', views.Module_7_Lesson_2.as_view(), name='module-7-lesson-2'),
    url(r'^top-bitcoin-resources/$', views.Module_7_Lesson_3.as_view(), name='module-7-lesson-3'),

    #api
    url(r'^api/comment/$', views.CommentAPI.as_view(), name='comment-api'),
    url(r'^api/subcomment/$', views.SubCommentAPI.as_view(), name='subcomment-api'),
]
