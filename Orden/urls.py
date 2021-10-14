from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.get_orden),
    path('<int:id>/update/', views.prueba)
]