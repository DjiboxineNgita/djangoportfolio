from myapp import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns=[
        path('index/', views.index, name='index'),
        path('presentation/', views.presentation, name='presentation'),
        path('realisation/', views.realisation, name='realisation'),
        path('competence/', views.competence, name='competence'),
        path('contact/', views.contact, name='contact'),
        path('loisirs/', views.loisirs, name='loisirs'),
        path('observation/', views.observation, name='observation'),
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', views.logoutView, name='logout'),
        path('signup/', views.signup, name='signup'),
]