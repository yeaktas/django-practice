from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponseNotFound

# Create your views here.

data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web gelistirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

#http://127.0.0.1:8000/kurslar

def index(request):
    return render(request, 'courses/index.html')

def list(request):
    return HttpResponse('list')

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} kurs detay sayfasi')

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound('yanlis kategori secimi')

def getCoursesByCategoryId(request, category_id):

    return HttpResponse(f'kategori id: {category_id}')

