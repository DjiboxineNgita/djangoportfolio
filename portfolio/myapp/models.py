from django.db import models
from django.contrib.auth.models import User
from django import forms

class Observation(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class VisiteurFroms(forms.Form):
    nom = forms.CharField(max_length=50,error_messages={'required':'champ obligatoire'})
    Poste = forms.IntegerField()
    date = forms.DateTimeField(auto_now_add=True)