from django.urls import path
from .views import IndexView
urlpatterns =[
    #path('endereco/', Minhaview.as_view, name = 'nome-da-url')
    path('inicio/', IndexView.as_view(), name = 'inicio'), 
    
]