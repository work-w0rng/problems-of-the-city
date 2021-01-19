from ninja import Schema


class User(Schema):
    full_name: str
    address: str = None
    email: str
    password: str


class Token(Schema):
    token: str


class Error(Schema):
    message: str
