from django.urls import path
from . import views

urlpatterns = [
    path('', views.Base, name='base'),
    path('index.html/', views.Page, name='index'),
    path('post/<int:id>', views.Postview, name='postview'),
]