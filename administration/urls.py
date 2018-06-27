from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),

    #user management
    url(r'^user/all/$', views.AllUser.as_view(), name='all-user'),
    url(r'^user/detail/(?P<user_id>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^user/(?P<user_id>[0-9]+)/edit/$', views.EditUser.as_view(), name='edit-user'),
    url(r'^user/(?P<user_id>[0-9]+)/change-password/$', views.ChangeUserPassword.as_view(), name='change-user-password'),
    url(r'^user/(?P<profile_status>[a-zA-z]+)/(?P<user_id>[0-9]+)/$', views.ActiveDeactiveUser.as_view(), name='active-deactive-user'),
    url(r'^user/(?P<user_id>[0-9]+)/delete/$', views.DeleteUser.as_view(), name='delete-user'),

    url(r'^user/(?P<user_id>[0-9]+)/referral/$', views.UserReferral.as_view(), name='user-referral'),

    url(r'^user/(?P<user_id>[0-9]+)/change-membership/$', views.ChangeMembership.as_view(), name='change-membership'),


    #payment operations
    url(r'^payment/$', views.PaymentManagement.as_view(), name='payment-management'),
    url(r'^payment/pending/$', views.PaymentPending.as_view(), name='payment-pending'),
    url(r'^payment/(?P<payment_id>[0-9]+)/detail/$', views.PaymentDetail.as_view(), name='payment-detail'),

    #commissions payout
    url(r'^commission-payment/$', views.CommissionPayment.as_view(), name='commission-payment'),
    url(r'^commission-payment/(?P<commission_id>[0-9]+)/detail/$', views.CommissionPaymentDetail.as_view(), name='commission-payment-detail'),



    #course management home
    url(r'^course/$', views.CourseManagement.as_view(), name='course-management'),


    #url for module control
    url(r'^module-control/$', views.ModuleControl.as_view(), name='module-control'),

    #url for lesson control
    url(r'^lesson-control/$', views.LessonControl.as_view(), name='lesson-control'),
    url(r'^lesson-detail/(?P<module_id>[0-9]+)/$', views.LessonDetail.as_view(), name='lesson-detail'),

    #url for step control
    url(r'^step-control/$', views.StepControls.as_view(), name='step-control'),

    #url for control affiliate link
    url(r'^affiliate-link-control/$', views.AffiliateLinkControls.as_view(), name='affiliate-link-control'),

    #add video on lesson
    url(r'^video/add/$', views.AddVideo.as_view(), name='add-video'),


    #latest webinar link
    url(r'^webinar-registration/link/$', views.WebinarRegistrationLink.as_view(), name='webinar-registration-link'),


    #leader board creation
    url(r'^leader-board/create/$', views.CreateLeaderBoard.as_view(), name='create-leader-board'),
    url(r'^leader-board/(?P<campaign_name>[0-9A-Za-z-_]+)/view/$', views.ViewLeaderBoard.as_view(), name='view-leader-board'),

    url(r'^leader-board/referral/$', views.LeaderBoardReferral.as_view(), name='leader-board-referral'),



    #recent update post for dashboard
    url(r'^recent-update/$', views.RecentUpdateHome.as_view(), name='recent-update-home'),
    url(r'^recent-update/post/$', views.RecentUpdatePost.as_view(), name='recent-update-post'),
    url(r'^recent-update/post/all/$', views.RecentUpdatePostAll.as_view(), name='recent-update-post-all'),
    url(r'^recent-update/post/(?P<post_id>[0-9]+)/detail/$', views.RecentUpdatePostDetail.as_view(), name='recent-update-post-detail'),
    url(r'^recent-update/post/(?P<post_id>[0-9]+)/edit/$', views.RecentUpdateEditPost.as_view(), name='recent-update-post-edit'),
    url(r'^recent-update/post/(?P<post_id>[0-9]+)/delete/$', views.RecentUpdateDeletePost.as_view(), name='recent-update-post-delete'),


    #update live video link
    url(r'^live-stream/link/add/$', views.LiveVideoLinkUpdate.as_view(), name='live-video-link-update'),


]
