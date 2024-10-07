from django.urls import path
from estoque.views import estoque

urlpatterns = [
    path('', estoque, name='estoque'),
]