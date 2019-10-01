from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import PasswordReset


User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', required=True)

    # ELE RECEBE O EMAIL DIGITADO NO POST DEPOIS FILTRA E BUSCA O VALOR NOS CAMPOS DO BANCO
    # SE RETORNAR TRUE ELE DA O ERRO E NAO PROSEGUE, SE NAO ELE RETORNA O EMAIL NORMAL E PROSEGUE
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('JÁ EXISTE USUARIO COM ESTE EMAIL')
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Nenhum e-mail encontrado!')



class EditAccountForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        # busca no banco se ja existe email.
        # o exclude nao deixa verificar o proprio email da pessoa, ja que ela tem cadastro no sistema.
        query_set = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if query_set.exists():
            raise forms.ValidationError('JÁ EXISTE USUARIO COM ESTE EMAIL')
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'name')