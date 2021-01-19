from os import path, mkdir


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ninja',
]

LOCAL_APPS = [
    'apps.users'
]

INSTALLED_APPS += LOCAL_APPS

LOCAL_APPS_NAME = [app_path.split('.')[1] for app_path in LOCAL_APPS]

MIGRATION_PATH = 'config.migrations'

MIGRATION_MODULES = {
    app_name: f'{MIGRATION_PATH}.{app_name}'
    for app_name in LOCAL_APPS_NAME
}
