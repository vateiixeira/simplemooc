from django.urls import path
from .views import index, details,enrollment,announcements

app_name='courses'

urlpatterns = [
    path('', index, name='index_cursos'),
    # path('<int:pk>', details , name='details'),
    path('<slug:slug>/', details, name='details'),
    path('<slug:slug>/inscricao/', enrollment, name='enrollment'),
    path('anuncios/<slug:slug>/', announcements, name='announcements')
]