from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.conf import settings
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from simplemooc.core.utils import generate_hash_key
from .models import PasswordReset
from simplemooc.courses.models import Enrollment, Courses
from simplemooc.core.utils import generate_hash_key
from simplemooc.core.mail import send_mail_template
from django.contrib import messages

User = get_user_model()

# ELE REDIRECIONA ESSA VIEW VERIFICANDO SE TA LOGADO, SE NAO TIVER ELE SAI E VOLTA PRA ROME CONFORME OS SETTINGS
@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)

@login_required
def editar(request):
    template_name = 'editar.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados alterados com sucesso.')
            return redirect('accounts:dashboard')
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)

def passreset(request):
    context = {}
    template_name = 'password-reset.html'
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(email=form.cleaned_data['email'])
        # instancia e-mail para passar pra outra formula
        emailusuario = user.email
        key = generate_hash_key()
        salvainstancia = PasswordReset(key=key, username=user)
        salvainstancia.save()
        context['confirma'] = True
        # ENVIO DE EMAIL
        subject = 'Redefinicao de senha. Simple MOOC'
        template_name_mail = 'password_reset_mail.html'
        context_mail = {
            'salvainstancia': salvainstancia
        }
        send_mail_template(subject, template_name_mail, context_mail, [emailusuario])
    context['form'] = form
    return render(request, template_name, context)

def passreset_confirm(request, key):
    template_name = 'password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.username, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['confirma'] = True
    context['form'] = form
    return render(request, template_name, context)

@login_required
def passchange(request):
    template_name = 'passchange.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # atualiza os campos salvos
            context['sucess'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


def register(request):
    template_name= 'register.html'
    # se for um metodo POST ele recebe os dados que veio da digitacao
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # CHAMA O FORM DO USUARIO E SALVA NO BANCO
            user = form.save()
            #user = authenticate(username=form.cleaned_data['username'], password = form.cleaned_data['password2'])
            # coloca usuario na sessao
            login(request,user)
            # SALVA O FORMULARIO E REDIRECIONA PARA LOGIN_URL DEFINIDO NO SETTINGS
            return redirect('core:home')
    else:
        form = RegisterForm()

    context= {'form': form}
    return render(request,template_name,context)




