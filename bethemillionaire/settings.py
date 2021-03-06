import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'o-acz@*s1_-wixn+1f-g8to38s8h@y%=+w)hyop&xsutdg=ua4'

DEBUG = True

ALLOWED_HOSTS = ['138.68.161.80', 'bethemillionaire.com', 'www.bethemillionaire.com']
#ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'paypal.standard.ipn',

    'home.apps.HomeConfig',
    'account.apps.AccountConfig',
    'payment.apps.PaymentConfig',
    'topic.apps.TopicConfig',
    'course.apps.CourseConfig',
    'lessons.apps.LessonsConfig',
    'administration.apps.AdministrationConfig',

    'django_celery_beat',
    'django_celery_results',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'bethemillionaire.middleware.LoginRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bethemillionaire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bethemillionaire.wsgi.application'

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'be_themillionaire',
        'USER': 'root',
        'PASSWORD': 'Nstu12345678~!',
        'HOST': '46.101.14.199',
    }
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'be_themillionaire',
        'USER': 'postgres',
        'PASSWORD': 'nstu12345678',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}"""


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



AUTHENTICATION_BACKENDS = (
    'account.models.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)




"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # mail service smtp
EMAIL_HOST_USER = 'mubarak117136' # email id
EMAIL_HOST_PASSWORD = '117136m117136u' #password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # mail service smtp
EMAIL_HOST_USER = 'support@bethemillionaire.com' # email id
EMAIL_HOST_PASSWORD = 'menaKP00' #password
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'bethemillionaire/media')

LOGIN_URL = '/account/registration/'

LOGIN_EXEMPT_URLS = (
 r'^admin/$',
 r'^account/login/$',


 r'^live/([0-9a-zA-Z.-]+)/$',
 r'^live-chat-message/([0-9a-zA-Z.-_]+)/$',


 r'^topic/step-1-overview/$',
 r'^topic/step-2-set-up-your-bitcoin-wallet-load-it-with-bitcoins/$',

 r'^account/pre-registration/$',
 r'^account/registration/$',

 r'^account/latest-webinar/$',


 r'^account/pre-web/$',
 r'^account/reg-web/$',
 r'^account/web-confirmation/$',


 r'^account/webinar/$',
 r'^account/live-web-class/$',
 r'^account/watchlivewebclass/$',


 r'^account/get-your-course/$',


 r'^account/secrets-to-wealth/$',
 r'^account/secrets-to-wealth-final/$',

 r'^account/webinar-replay/$',


 r'^account/pre-usi/$',
 r'^account/reg-usi/$',
 r'^account/usi-2/$',
 r'^account/usi-tech-fast-start/$',


 r'^account/usi/$',


 r'^account/bitconnect/$',
 r'^account/bcc-fast-start/$',


 r'^account/7-figure-strategies/$',


 r'^account/how-to-set-up-your-btm-system/$',


 r'^account/7-figure-plan/$',

 r'^account/7-figure-plan/$',


 r'^account/api/check-username/$',

 r'^account/access/$',
 r'^account/welcome/$',
 r'^account/thank-you/$',

 r'^account/api/user-profile/$',


 r'^account/paypal-ipn/$',

 r'^account/recover-password/$',
 r'^account/recover-password/done/$',
 r'^account/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
 r'^account/reset/done/$',

 r'^static/account/style/([0-9a-zA-Z.-]+)$',
 r'^static/account/js/([0-9a-zA-Z.-]+)$',
 r'^static/home/js/([0-9a-zA-Z.-]+)$',

 r'^media/images/user/([0-9a-zA-Z.-_]+)$',

)


#django-paypal settings
PAYPAL_RECEIVER_EMAIL = 'sharifulislam.cs@gmail.com'
PAYPAL_TEST = False



REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}


AUTH_USER_MODEL = 'account.UserProfile'

#SECURE_SSL_REDIRECT = True

"""
CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True
"""

#redis config
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE



# Channels
ASGI_APPLICATION = 'bethemillionaire.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


ASGI_APPLICATION = "bethemillionaire.routing.application"
