from django.urls import path
from departamento.views import index

urlpatterns = [
    path('', index, name='departamento.index')
]