from django.shortcuts import render
from django.http import HttpResponse

def about_me(request):
    return render(request, 'personal/about.html')

def index(request):
    return render(request, 'personal/index.html')

def Online_Shopping(request):
    return render(request, 'personal/OnlineShopping.html')

