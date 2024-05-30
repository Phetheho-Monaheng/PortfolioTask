from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_me, name='about'),
    path('index/', views.index, name='index'),
    path('OnlineShopping/', views.Online_Shopping, name='OnlineShopping'),
]
