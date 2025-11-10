from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #path('<int:id>/', views.post_detail),
    #path('<slug:category_slug>/', views.category_posts),
]