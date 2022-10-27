from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    
    path('', home), #HOME
    path('sobre/', sobre),  #/SOBRE/
    path('contato/', contato), #/contato/
]
