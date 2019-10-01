from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('simplemooc.core.urls')),
    path('contas/', include('simplemooc.accounts.urls')),
    path('cursos/', include('simplemooc.courses.urls')),
    path('admin/', admin.site.urls),
    path('villefort/', include('simplemooc.datahora.urls'))
]
# SE DEBUG FOR VERDADEIRO, OU MELHOR, SE DEBUG ESTIVER ATIVO NOS SETTINGS.
if settings.DEBUG:
    # REDIRECIONA TODAS AS URLS E GERA UM CAMINHO DE ARQUIVO PARA ALOCAR OAS IMAGENS
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


