from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_ingredients', views.search_ingredients, name='search_ingredients')
]