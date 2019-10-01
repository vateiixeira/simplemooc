from django.contrib import admin
from .models import Courses

class CourseAdmin(admin.ModelAdmin):
    # CRIA DISPLAY DE VISUALIZACAO DOS CAMPOS EXISTENTES NESSA TABELA
    list_display = ['name', 'slug', 'start_date', 'create_at']
    # CAMPO PARA PESQUISAR . SE CONTEM
    search_fields = ['name','slug']
    # CRIA CAMPO SLUG RITRANDO ACENTO E ESPAÇOS
    prepopulated_fields = {'slug' : ['name']}


admin.site.register(Courses, CourseAdmin)



