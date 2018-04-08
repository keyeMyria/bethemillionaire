import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'o-acz@*s1_-wixn+1f-g8to38s8h@y%=+w)hyop&xsutdg=ua4'

DEBUG = True

ALLOWED_HOSTS = []


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
        'NAME': 'databasbethemillionaire',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
    }
}
"""


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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # mail service smtp
EMAIL_HOST_USER = 'mubarak117136' # email id
EMAIL_HOST_PASSWORD = '117136m117136u' #password
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

 r'^account/pre-registration/$',
 r'^account/registration/$',


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
