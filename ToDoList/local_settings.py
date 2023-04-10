from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo',
        'USER': 'postgres',
        'PASSWORD': 'trololo228',
        'HOST': 'localhost',
        'PORT': '',
    }
}