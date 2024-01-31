from datetime import date
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

db = {

    "courses": [

        {
            "title": "javascript kursu",
            "description": "javascript kursu aciklamasi",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/1662526_fc1c_3.jpg",
            "slug": "javascript-kursu",
            "date": date(2024, 1, 1),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "python kursu",
            "description": "python kursu aciklamasi",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/2463492_8344_3.jpg",
            "slug": "python-kursu",
            "date": date(2024, 1, 1),
            "isActive": False,
            "isUpdated": False
        },
        {
            "title": "web gelistirme kursu",
            "description": "web gelistirme kursu aciklamasi",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2024, 1, 1),
            "isActive": True,
            "isUpdated": True
        }
    ],

    "categories": [
        {"id": 1 , "name": "programlama", "slug": "programlama"}, 
        {"id": 2 , "name": "web gelistirme", "slug": "web-gelistirme"}, 
        {"id": 3 , "name": "mobil uygulamalar", "slug": "mobil-uygulamalar"}
        ]
}


#http://127.0.0.1:8000/kurslar

def index(request):
    #list comprehension
    kurslar = [course for course in db["courses"] if course["isActive"] == True]
    kategoriler = db["categories"]

    #for kurs in db["courses"]:
    #    if kurs["isActive"]:
    #        kurslar.append(kurs)

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar,
    })

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} kurs detay sayfasi')

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'courses/courses.html', {
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound('yanlis kategori secimi')

def getCoursesByCategoryId(request, category_id):

    return HttpResponse(f'kategori id: {category_id}')

