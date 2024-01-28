from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kurslar(request):
    return HttpResponse('kurslar')

def list(request):
    return HttpResponse('list')

def programlama(request):
    return HttpResponse('programlama')

def getCoursesByCategory(request, category_name):

    text = ""

    if(category_name == "yazilim"):
        text = "Yazilim Kurslari"
    elif(category_name == "tasarim"):
        text = "Tasarim Kurslari"
    else:
        text = "Yanlis kategori"

    return HttpResponse(text)
    #return HttpResponse(f'{category} kategorisindeki kurs listesi')
