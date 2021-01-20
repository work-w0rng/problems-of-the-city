from ninja import Schema
from typing import List


class Registration(Schema):
    full_name: str
    address: str = None
    email: str
    password: str


class Token(Schema):
    token: str


class Error(Schema):
    """
    **email_already_use**: на данную почту уже зарегистрирован аккаунт;

    **password_too_short**: введенный пароль сильно короткий;

    **password_entirely_numeric**: пароль состоит только из цифр;
    
    **invalid_email**: введен некорректный email

    **invalid_full_name**: неправильный формат ФИО
    """
    codes: List[str]


class Login(Schema):
    email: str
    password: str


class ResetPassword(Schema):
    new_password: str
