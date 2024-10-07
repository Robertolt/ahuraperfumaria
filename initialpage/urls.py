from django.urls import path
from initialpage.views import index, areadogerente, login, sair

urlpatterns = [
    path('', index, name='index'),
    path('areadogerente/', areadogerente, name='areadogerente'),
    path('login/', login, name='login'),
    path('sair/', sair, name='sair'),
]