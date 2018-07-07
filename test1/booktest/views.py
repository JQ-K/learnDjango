from django.shortcuts import render
from  django.http import *
from django.template import RequestContext, loader
from models import *

# Create your views here.


def index(request):   
    #temp = loader.get_template('booktest/index.html')
    #return HttpResponse(temp.render())
    book_list = BookInfo.objects.all()
    context = {'list': book_list}
    return render(request, 'booktest/index.html',context)


def show(request,id):
    book =  BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    content = {'list':herolist}
    return render(request, 'booktest/show.html', content)
