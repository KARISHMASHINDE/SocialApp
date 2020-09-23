from django.urls import path
from . import views 


urlpatterns = [
  path('',views.index),
  path('about/',views.about,name='about'),
  path('home/',views.home,name='home'),
  path('events/',views.event,name='events'),

  
]