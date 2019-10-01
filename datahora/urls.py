from django.urls import path
from .views import datahora

app_name='datahora'

urlpatterns = [
    path('home', datahora, name='home'),
]