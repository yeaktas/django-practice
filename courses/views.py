from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponseNotFound, Http404
from . models import Course, Category

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
            "imageUrl": "1.jpg",
            "slug": "javascript-kursu",
            "date": date(2024, 1, 1),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "python kursu",
            "description": "python kursu aciklamasi",
            "imageUrl": "2.jpg",
            "slug": "python-kursu",
            "date": date(2024, 1, 1),
            "isActive": False,
            "isUpdated": False
        },
        {
            "title": "web gelistirme kursu",
            "description": "web gelistirme kursu aciklamasi",
            "imageUrl": "3.jpg",
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
    #kurslar = [course for course in db["courses"] if course["isActive"] == True]
    #kategoriler = db["categories"]
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    #for kurs in db["courses"]:
    #    if kurs["isActive"]:
    #        kurslar.append(kurs)

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar,
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

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

