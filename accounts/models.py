from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.conf import settings


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Nome do Usuario', max_length=100, unique=True,
        validators = [validators.RegexValidator((r'^[\w.@+-]+\Z'),
        ('O nome de usuário só pode conter letras e esses caracteres: @ . / - + - _'))])
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True,default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)

    #acessa o user manager, responsavel por capturar os dados existentes na tabela
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class PasswordReset(models.Model):
    username = models.ForeignKey(User,
    on_delete = models.CASCADE, 
    verbose_name = 'Usuário',
    # campo criado para relcionar a chave estrangeira e capturar dados da outra tabela
    related_name = 'resets')
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado', default=False, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova senha'
        verbose_name_plural = 'Novas senhas'
        #parametro da classe meta que pode indicar o ordenamento padrao 
        ordering = ['-created_at']