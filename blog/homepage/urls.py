from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
 
    path('', views.index, name = 'home'),
    path('feed/', views.newsFeed, name = 'feed'),

]