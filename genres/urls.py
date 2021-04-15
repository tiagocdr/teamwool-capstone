from django.urls import path
from genres import views

urlspatterns = [
    path('automotive/', views.automotive_view, name='autos'),
    path('arts/', views.arts_view, name='arts'),
    path('climatechange/', views.cc_view, name='cc'),
    path('dadjokes/', views.dadjokes_view, name='dad jokes'),
    path('opinion/', views.opinion_view, name='opinion'),
    path('politics/', views.politics_view, name='politics'),

]