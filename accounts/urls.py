from django.urls import path
from django.conf.urls import include,url
from django.contrib.auth.views import LoginView, LogoutView
from .views import register,dashboard,editar,passchange,passreset, passreset_confirm

app_name='accounts'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', LoginView.as_view(), {"template_name" : "accounts/login.html"}, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page = 'core:home'), name='logout'),
    path('editar/', editar, name='editar'),
    path('passchange/', passchange, name='passchange'),
    path('passreset/', passreset, name='passwordreset'),
    path('confirm-passreset/<key>/', passreset_confirm, name='passreset_confirm')
]
