from os import environ


DEBUG = environ.get('DEBUG', True)
SECRET_KEY = environ.get('SECRET_KEY', 'secret_key')
ADMIN_URL = environ.get('ADMIN_URL', 'admin/')
