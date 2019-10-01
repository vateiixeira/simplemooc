from django import forms

class CaixaHora(forms.Form):
    dia = forms.IntegerField(label='Dia')
    mes=forms.CharField(label='Mes')
    ano=forms.IntegerField(label='Ano')
    nota = forms.IntegerField(label='Nota')