from django.db import models
class Visiteur(models.Model):
    nom = models.CharField(max_length=50)
    observations = models.CharField(max_length=50)
    poste = models.CharField(max_length=50)