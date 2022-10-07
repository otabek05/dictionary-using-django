from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat

# Create your views here.
def index(request):
    word=request.GET.get('q', ' Search')
    
    if word and word != ' ':
        result=Lugat.objects.filter(inglizcha=word).all()
    else:
        result=None
    return render(request, 'index.html',{'q': word, 'result':result})

def index1(request):
    word2=request.GET.get('h', 'Search')
    if word2 and word2 != '':
        result=Lugat.objects.filter(inglizcha=word2).all()
    else:
        result='Not ffound from database'
    return render(request, 'index2.html',{'h':word2, 'result':result})
