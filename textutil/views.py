#i have created this file
from django.http import *
from django.shortcuts import *
def index(req):
    return render(req,'index.html')
#def removepunc(req):
 #   print(req.GET.get('text','default'))
  #  print(req.GET.get('removepunc','off'))
   # return HttpResponse("remove punc<button><a href='/'>go back</a></button>")'''
def capfirst(req):
    return HttpResponse("capfirst<button><a href='/'>go back</a></button>")
def newlineremove(req):
    return HttpResponse("newline<button><a href='/'>go back</a></button>")
def spaceremover(req):
    return HttpResponse("space<button><a href='/'>go back</a></button>")
def analize(req):
    print(req.POST.get('text', 'default'))
    text=req.POST.get('text', 'default')
    val=req.POST.get('removepunc', 'off')
    fullcaps=req.POST.get('fullcaps','off')
    print(req.POST.get('removepunc', 'off'))
    punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analized_text=''
    if val=='on':
     for i in text:
        if i in punc:
            continue
        analized_text+=i
     if fullcaps=='on':
         analized_text=analized_text.upper()
    params={'text':text,'analized_text':analized_text}
    return render(req,'analize.html',params)
def aboutus(req):
    return render(req,'aboutus.html')
def contactus(req):
    pass