from django.urls import path
from . import views

urlpatterns = [
    path('', views.kurslar),
    path('list', views.kurslar),
    path('<kurs_adi>', views.details),
    path('kategori/<int:category_id>', views.getCoursesByCategoryID),
    path('kategori/<str:category_name>', views.getCoursesByCategory),
]