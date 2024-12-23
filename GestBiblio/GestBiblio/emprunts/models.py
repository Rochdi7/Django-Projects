from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from livres.models import Livre

class Emprunt(models.Model):
    emprunteur = models.CharField(max_length=100)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField()

    def clean(self):
        if self.livre.exemplaires <= 0:
            raise ValidationError(f"Le livre '{self.livre.titre}' n'est pas disponible pour l'emprunt.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Emprunt de {self.emprunteur} - {self.livre.titre}"

