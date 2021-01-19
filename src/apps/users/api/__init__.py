from ninja import Router


router = Router()

"""
Небольшой костыль, чтобы заставить ninja работать с модулем api в виде папки, а
не файла, как рекомендует документация
"""

from .views import *
