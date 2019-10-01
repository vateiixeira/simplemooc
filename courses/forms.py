from django import forms
from django.core.mail import send_mail
from django.conf import settings
from simplemooc.core.mail import send_mail_template

# CLASSE PARA CRIAR CAMPOS DO FORMULARIO
class ContactCourses(forms.Form):
    name = forms.CharField(label= 'Nome', max_length=100)
    email = forms.EmailField(label= 'Email')
    # WIDGET É RESPONSAVEL PELA RENDERIZAC AO, NO CASO TEXTAREA SERVE PRA AUMENTAR O TAMANHO DO CAMPO DE TEXTO, JA QUE NAO EXISTE TEXT.FIELD
    message = forms.CharField(label= 'Dúvidas/Mensagem', widget=forms.Textarea)

    def send_mail(self, courses):
        subject = f'Duvida sobre o curso: {courses}'
        # CAPTURA OS DADOS DIGITADOS NO FORUMALARIO.. ****** VERIFICAR MELHOR
        context = {
            "name" : self.cleaned_data['name'],
            "email" : self.cleaned_data['email'],
            "message" : self.cleaned_data['message']}
        template_name = 'courses/contact_email.html'
        # COMANDO PADRONIZADO PARA ENVIAR EMAIL.
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )