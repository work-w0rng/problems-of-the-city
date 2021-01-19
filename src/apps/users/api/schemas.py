from ninja import Schema


class User(Schema):
    full_name: str
    address: str = None
    email: str
    password: str
