from django.db import models
from django.urls import reverse

# Create your models here.
class Letter(models.Model):
    nom = models.CharField("Nom du client", max_length=50)
    email = models.CharField("Addresse mail", max_length=50)
    numerofact = models.PositiveSmallIntegerField("Numéro de Facture", unique=True)
    
    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("letter_detail", kwargs={"pk": self.pk})

