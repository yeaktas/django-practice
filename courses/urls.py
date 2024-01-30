from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list', views.index),
    path('<kurs_adi>', views.details),
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),
    path('kategori/<str:category_name>', views.getCoursesByCategory),
]