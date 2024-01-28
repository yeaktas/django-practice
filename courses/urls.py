from django.urls import path
from . import views

urlpatterns = [
    path('', views.kurslar),
    path('list', views.kurslar),
    path('programlama', views.programlama),
    path('<category_name>', views.getCoursesByCategory)
]