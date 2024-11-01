from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_example/', views.add_example),
    path('edit_example/<int:id>/', views.edit_example),
    path('delete_example/<int:id>/', views.delete_example),
]