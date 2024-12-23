from django.db import models

# Create your models here.
from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)
    date_naissance = models.DateField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"
