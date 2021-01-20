from .validators import validate_full_name


def convert_full_name(value) -> str:
    """
    Конвертация ФИО

    Переводит ФИО формата 'Фамилия Имя Отчество' в формат 'Фамилия. И. О.'
    Если же отчество отсутствует, вернет Фамилия. И.
    """
    validate_full_name(value)

    if value.count(' ') == 1:
        surname, name = value.split(' ')
        return f'{surname} {name[0]}.'

    surname, name, middle_name = value.split(' ')
    return f'{surname} {name[0]}. {middle_name[0]}.'
