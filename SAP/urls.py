from django.urls import path
from . import views

urlpatterns = [
    path('', views.SAPApi),
    path('<int:id>/', views.SAPApi)
]