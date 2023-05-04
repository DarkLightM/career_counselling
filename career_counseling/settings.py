import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mxw*4j7q%sklpph7p6hxr5@s%j4lka4&ooa)(_u@#hd#e2(^1c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'profiles.apps.ProfilesConfig',
    'transcriber.apps.TranscriberConfig',
    'vk_info.apps.VkInfoConfig',
    'analytics.apps.AnalyticsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'career_counseling.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'career_counseling.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SERVICE_ACCOUNT_ID = 'aje4t0n9j7o3i3lm0lvb'
YANDEX_PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDMb0Rac1wklhGF\nSykB/GVBlSIv8MObSTsS8eOgy3UYYuhGuNBCKhxliBfPowpySm0egoXJIibugigq\nQpzCyktUQ4bV4wrywPbiE6U6grnvxcdZscmh0Z6jBt4TIglZrsuF/xpMwcw03tpQ\n7tzNaB34lloIO8zQe9ZJybG7NpS8DlB1tgkETPIIFMKG0Zpw+XPhrsZWqyegM7st\nCReDuhqSN5iJ89XbgDBvFBKYjtMZ5Ol63xkwxITdxoS6S5cyCe5A0SDm3siVaRa9\nQEfhMpgY04ecnKWG+o2l28taCOajC1rYdqCFflCWLfczHmT6y60Qq5dTBVkavF00\nEfmak7UZAgMBAAECggEABXloRuobuktox4fiSVA+ejcEXezFoXj185VVxKvrZDOy\nfRb8qqeRMEMol2c0rn1MNpAvsBmxmbA+DkL6NXlwcslGc8qbM9y+GlfaKZAvwETX\nSFFWBnbZbOD68t+13jiA8Nhf1lTX2JrsFSqO7+gnv0zwDGmPho3+XbugflR2lKIw\nOX9Ml107jvU/INVPHob+/JtsOETiSLlPz+qqR4I/NeihYm9ylsYWC3sjytAq9CJv\nl0ftZwE9f2Bnw38Do9VZxgNpfzjn9CCqIumbNUr9A852mTvNKRyMKS0kpmEV54/3\nt32CgeoH8rZMhWKIeS2ybeRnBE0qIkEj3VKGqgQftQKBgQDZM9sWyw9JGskHoWsu\nKjY8DXqv4REWAnm2BIbgT5SCnXAQNaFJxd4AB1Z4UXkuiS+wz5D23yJ7ubTrNEJf\nCrdGdMkvE+4/SqGyANKx8RRrXuXGcn9RkKsq1N1w1CyIj7h1OzVteIyz3409/EnI\nLpKOxmb3kvylhC5CKkMi7Tc5jQKBgQDw85Coe9vfoHvxDZLfl0HP3XrTiQAWzaUh\nXTKNDPN3Ir3J/P3Zvkbozo5iVDgdn1katWqmfggG4xhf56KTaLaNfHowMMzw9NEB\n0iomLN7t2OTh0vsAdf57f14+Y9AlPDljguQbS8lPSm/epBiGtx6ER+K681f7evHR\nmGSt7E0YvQKBgQCISVN1j+B9fIMbeJuqEe6J6+NJrK1t5Au+vERtR0HmWydP5HbZ\ntYBBAFmvkV+6ZXY5OWS6ovQeMj5lPxtOS4kIeosqMRVTPV8MNBwAb0biwF7pEDr3\nURE2BO8Vtuxim9ugI5C4qeWPj/wuIrmhFCf90lwViHNi3/euqJoLtlDqmQKBgQCU\nRq68oAv8n/vlqV667Y/4ZOlTB7ngTojR8VJMbq3coKp+hIuK1Yc5ePMyG3W09PyW\nbRHGh0RVSKcVTaxEXmoIw5NF2KIlneKI5lY9y9scLx8awQTpkbMbOJQ8fJv4bgk6\n7a+GBKtLehlBv2XAcSv8Z2hld56rCUuKmedLCGGhWQKBgBLOMKu0f7J8y1UBz1oW\ni4S7anA2vaHrQfNcYM5uZB9bzZu3sBQdIPanMJW0iKmbqwuT/BUH+cA3tC1Ye9Cg\ngUlT7Ff8Tz2Jyo2w8xVsXo+vNA7RuGuyLRk0r5z9OOeDWT76XoX1T0c0k9BusBbQ\ndln4HCkSdDDJrM6JPv4TBp1W\n-----END PRIVATE KEY-----\n"
YANDEX_KEY_ID = 'ajenm769pg13dmmp4i2o'
BUCKET_NAME = 'career-counseling'
