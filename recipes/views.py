from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



# http request
def home(request):
   return render(request, 'recipes/home.html', context={
    'name': 'Mauricio J Joaquim',
   })


   # http request
def sobre(request):
   return HttpResponse('SOBRE')


   # http request
def contato(request):
   return HttpResponse('CONTATO')
