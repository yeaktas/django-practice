from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kurslar(request):
    return HttpResponse('kurslar')

def list(request):
    return HttpResponse('list')

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} kurs detay sayfasi')

def getCoursesByCategory(request, category_name):

    text = ""

    if(category_name == "programlama"):
        text = "Programlama Kurslari"
    elif(category_name == "tasarim"):
        text = "Tasarim Kurslari"
    else:
        text = "Yanlis kategori"

    return HttpResponse(text)
    #return HttpResponse(f'{category} kategorisindeki kurs listesi')

def getCoursesByCategoryID(request, category_id):
    return HttpResponse(category_id)