from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from article.models import Article


def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request, my_args):
    post = Article.objects.all()[my_args]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
           % (post.title,post.category,post.date_time,post.content))
    return HttpResponse(str)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})