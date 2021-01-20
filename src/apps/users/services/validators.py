from django.utils.regex_helper import _lazy_re_compile
from django.core.exceptions import ValidationError


class FullNameValidator:
    message = 'Введите ФИО в корректном формате'
    code = 'invalid'
    fio_regex = _lazy_re_compile(
        r"[a-zA-ZА-Яа-яЁё\-]{2,}( [a-zA-ZА-Яа-яЁё]{2,}){1,2}"
    )

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not self.fio_regex.match(value):
            raise ValidationError(self.message, code=self.code)


validate_full_name = FullNameValidator()
