from myapp import views
from django.urls import path

urlpatterns=[
        path('index/', views.index, name='index'),
        path('presentation/', views.presentation, name='presentation'),
        path('realisation/', views.realisation, name='realisation'),
        path('competence/', views.competence, name='competence'),
        path('contact/', views.contact, name='contact'),
        path('loisirs/', views.loisirs, name='loisirs'),
        path('observation/', views.observation, name='observation')
]