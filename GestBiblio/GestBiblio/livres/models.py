# models.py
from django.db import models
from auteurs.models import Auteur

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)  # Relation avec Auteur
    date_publication = models.DateField()
    genre = models.CharField(max_length=100)
    exemplaires = models.PositiveIntegerField()

    def __str__(self):
        return self.titre
