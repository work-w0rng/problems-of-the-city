from os import path, mkdir


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = []

INSTALLED_APPS += LOCAL_APPS

LOCAL_APPS_NAME = [app_path.split('.')[1] for app_path in LOCAL_APPS]

MIGRATION_PATH = 'config.migrations'

MIGRATION_MODULES = {
    app_name: f'{MIGRATION_PATH}.{app_name}'
    for app_name in LOCAL_APPS_NAME
}

for app in LOCAL_APPS_NAME:
    if not path.exists(f'config/migrations/{app}'):
        mkdir(f'config/migrations/{app}')
        open(f'config/migrations/{app}/__init__.py', 'w+').close()
