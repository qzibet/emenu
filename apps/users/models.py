from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractModel


class User(AbstractUser, AbstractModel):
    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
