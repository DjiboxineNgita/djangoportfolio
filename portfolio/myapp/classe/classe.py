from django.db import models
from django.contrib.auth.models import User

class Observation(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    poste=models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
	
    def __str__(self):
        return self.title