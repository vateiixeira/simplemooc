from django.shortcuts import render
from .forms import CaixaHora
from simplemooc.datahora.conexao2 import convert,conecta


def datahora(request):
    template_name = 'data_hora.html'
    result = ''
    context={}
    if request.method == 'GET':
        form = CaixaHora(request.GET)
        if form.is_valid():
            dia = form.cleaned_data['dia']
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']
            nota = form.cleaned_data['nota']

            data= f'{dia}-{convert(mes)}-{ano}'

            conecta(data=data, nota=nota)
            context['result'] = result
            context['sucess']=True
    else:
        form=CaixaHora(request.POST)
    context['form']=form
    return render(request,template_name,context)