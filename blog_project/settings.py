import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '6+_(6czw@+gbm$5q@j6u#ubk^)19o&0+3wi!2u(%x^^y^!d(j#'

DEBUG = True

ALLOWED_HOSTS = ['167.71.228.15']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third_party_apps.
    'crispy_forms',
    # taggit
    'taggit',
    'imagekit', #forthumbnails
    # My_apps.
    'blog',
    'users.apps.UsersConfig',
    'footer',
]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location':  os.path.join(BASE_DIR, 'backup')}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'blog_project.wsgi.application'


if DEBUG:
    DATABASES = {

        'default': {

            'ENGINE': 'django.db.backends.postgresql_psycopg2',

            'NAME': 'ncc_buddies_com',

            'USER': 'postgres',

            'PASSWORD': 'admin123',

            'HOST': 'localhost',

            'PORT': '5432',

        }
    }
else:
    DATABASES = {

        'default': {

            'ENGINE': 'django.db.backends.postgresql_psycopg2',

            'NAME': 'ncc_buddies_com',

            'USER': 'admin',

            'PASSWORD': 'admin123',

            'HOST': 'localhost',

            'PORT': '',

        }
    }



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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Accra'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog:home'
LOGIN_URL = 'login'


# EMAIL_USE_TLS = True    
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'uttam11.velani11@gmail.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ADMIN_SITE_HEADER = "BUDDIES"

TIME_ZONE =  'Asia/Kolkata'



