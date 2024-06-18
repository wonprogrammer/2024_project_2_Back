from django.urls import path, include
from articles import views

urlpatterns = [
    path('', views.articleAPI, name='articleAPI'),
    path('<int:article_id>/', views.articleDetailAPI, name='articleDetailAPI'),
]