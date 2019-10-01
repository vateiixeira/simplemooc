from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Courses, Enrollment
from .forms import ContactCourses
from django.contrib import messages
# index do app courses
def index(request):
    # captura todos os dados da tabela e instancia na variavel
    courses = Courses.objects.all()
    template_name = 'courses/index.html'
    # dicionario criaro para retornar no render e nele contem as variaveis necessarias para mostrar visualizado
    context = {
        'courses' : courses
    }
    return render(request, template_name, context)

def details(request, slug):
    context = {}
    # instancia a busca la no banco Courses e retorna APENAS um valor: pk . Se nao ecnontrar chave no banco ele retorna uma 404
    course = get_object_or_404(Courses, slug=slug)
    # cria um dicionario para ser usado no front end
    if request.method == 'POST':
        # SE TIVER UM METODO POST NA PAGINA, A VARIALVEL POSTO RECEBE OS DADOS DESSE POST .
        form = ContactCourses(request.POST)
        if form.is_valid():
            form.send_mail(course)
            # JOGA VALOR IS VALID EM CONTEXTO PARA VERIFICAR ELA NO FRONT E MOSTRAR UMA RESPOSTA ADEQUEADA.
            # NO CASO, SE ELE RECEBEU UM FORMULARIO VALIDO, ELE RECEBE ESSA MSG E RETORNA COM UM IF NO FRONT.
            context['is_valid'] = True
            # print(form.cleaned_data)
            form = ContactCourses()
    else:
        form = ContactCourses()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)

@login_required()
def enrollment(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    if created:
        # enrollment.active()
        messages.success(request, message='Voce foi inscrito no curso!')
    else:
        messages.info(request, message='Voce ja esta inscrito no curso!')

    return redirect('accounts:dashboard')

@login_required
def announcements(request, slug):
    # INSTANCIA O CURSO PEGANDO SLUG
    course = get_object_or_404(Courses, slug=slug)
    # SE NAO FOR STAFF ELE EXECUTA ESSE SCRIPT
    # if not request.user.is_staff:
    #     INSTANCIA O ANUNCIO PELO CURSO EM QUESTAO
        # enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        # if not enrollment.is_approved():
        #     messages.error(request, 'Inscricao pendente.')
        #     return redirect('accounts:dashboard')
    template = 'announcements.html'
    context = {
        'course': course
    }
    return render(request, template, context)
