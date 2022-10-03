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
