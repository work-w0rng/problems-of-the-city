from ninja import Schema


class Registration(Schema):
    full_name: str
    address: str = None
    email: str
    password: str


class Token(Schema):
    token: str


class Error(Schema):
    message: str


class Login(Schema):
    email: str
    password: str
