# from pathlib import Path
# import os
# import pymysql
# pymysql.install_as_MySQLdb()



# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# TEMPLATE_DIR = BASE_DIR / 'Trvels' / 'templates'
# STATIC_URL = '/static/'

# # Quick-start development settings - unsuitable for production
# SECRET_KEY = 'django-insecure-k483xsd(sz&2%%u)51%f&k18d_k+6y8&1h%+g!o2s&ss6^i6p^'
# DEBUG = True
# ALLOWED_HOSTS = []
# SITE_ID = 1
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#         'django.contrib.sites',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.google',
#     'Trvels',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#      "whitenoise.middleware.WhiteNoiseMiddleware",  
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#    'allauth.account.middleware.AccountMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',  # Default authentication
#     'allauth.account.auth_backends.AuthenticationBackend',  # Required for social login
# ]

# ROOT_URLCONF = 'DD_Tours.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [TEMPLATE_DIR],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'DD_Tours.wsgi.application'

# # Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'tours',
#         'USER': 'root',
#         'PASSWORD': 'Pratishtha',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     }
# }
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': BASE_DIR / "my.sqlite3",
# #     }
# # }

# LOGIN_REDIRECT_URL = '/'   # Redirect after login
# LOGOUT_REDIRECT_URL = '/'  # Redirect after logout
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # Change to 'optional' or 'mandatory' if needed

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': ['profile', 'email'],
#         'AUTH_PARAMS': {'access_type': 'online'},
#     }
# }


# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# STATICFILES_DIRS = [BASE_DIR / 'Trvels' / 'static']

# # Media files (uploads)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'#email backend
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST = 'smtp.gmail.com' #smtp server address
# EMAIL_HOST_USER = 'pratishthabagohil.21.ce@iite.indusuni.ac.in'
# EMAIL_HOST_PASSWORD = 'priti2103'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# DEFAULT_TO_EMAIL = '@gmail.com'

# CONTACT_EMAIL = 'gohilpratishtha57@gmail.com'  

# CONTACT_EMAIL = 'gohilpratishtha57@gmail.com'  

import os
from pathlib import Path
import pymysql
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'Trvels' / 'templates'

# Security Settings
# IMPORTANT: Replace this with a secure, randomly generated secret key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-very-secure-secret-key-here')

# Debug should be False in production
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Allowed hosts for production
ALLOWED_HOSTS = [
    # Vercel-generated domain
    'dd-tours-8udcdjdxv-pratishthabagohils-projects.vercel.app',
    
    # Your custom domain (if you have one)
    # 'yourdomain.com',
    
    # Local development hosts
    'localhost',
    '127.0.0.1',
    
    # Vercel's default subdomains
    '.vercel.app',
    
    # Your project's Vercel preview domains
    'dd-tours.vercel.app',
]

# For extra flexibility, you can use environment variables
ALLOWED_HOSTS += os.environ.get('EXTRA_ALLOWED_HOSTS', '').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'Trvels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'DD_Tours.urls'

# Templates Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'DD_Tours.wsgi.application'

# Database Configuration
# Use environment variables for database credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'tours'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'ssl': {
                'ca': os.environ.get('DB_SSL_CA', ''),  # Optional SSL certificate path
            },
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
        'CONN_MAX_AGE': 3600,  # Connection persistent for 1 hour
    }
}

# Authentication Settings
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # Recommended to use 'mandatory' in production

# Social Account Providers
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    }
}

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'Trvels' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Add this for production deployments

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Security Enhancements
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'False') == 'True'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
