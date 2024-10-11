from django.shortcuts import render
from django.http import HttpResponse
from mapaguapi.models import Problem
# Create your views here.

def home(request):
    problems = Problem.objects.all().order_by('-id')
    return render(request, 'mapaguapi/pages/home.html', context={
        'problems': problems,
    })

def problem(request, id):
    problems = Problem.objects.filter(pk=id, is_published=True).order_by('-id').first() 
    return render(request, 'mapaguapi/pages/problem-detail.html', context={
        'problems': problems,
        'is_detail_page': True,
    })