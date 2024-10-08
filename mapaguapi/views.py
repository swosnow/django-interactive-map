from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'mapaguapi/pages/home.html')

def problem(request, id):
    
    return render(request, 'mapaguapi/pages/problem-detail', context={
        'problem': problem,
        'is_detail_page': True,
    })