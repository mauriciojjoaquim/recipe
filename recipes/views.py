from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



# http request
def home(request):
   return render(request, 'recipes/pages/home.html', context={
    'name': 'Mauricio J Joaquim',
   })
