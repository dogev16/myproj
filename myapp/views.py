from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
def sayhello(request):
    return HttpResponse("hello dog")
def hello2 (requset,username):
    return HttpResponse("Hello " + username)
def hello3 (requset,username):
    now=datetime.now()
    return render(requset,"hello3.html",locals())
def hello4 (requset,username):
    now=datetime.now()
    return render(requset,"hello4.html",locals())



