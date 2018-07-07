from django.shortcuts import render
from models import *
# Create your views here.

def index(request):
    #hero = HeroInfo.objects.get(pk=1)
    #context = {'hero':hero}
    list = HeroInfo.objects.filter(isDelete=False)
    context = {'list': list}
    return render(request,'index.html', context)

def show(request, id, id2):
    context = {'id':id}
    return render(request, 'show.html',context)
