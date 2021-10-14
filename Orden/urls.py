from django.urls import path
from . import views

urlpatterns = [
    path('', views.ordenAPI),
    path('<int:id>', views.ordenAPI),
]