from django.db import models

# Create your models here.

class CarteGraphique(models.Model):
    nommodel = models.CharField(max_length=50)
    categorie = models.CharField(max_length=50)
    date_sortie = models.DateField(blank = True, null = True)
    qtevram = models.IntegerField(blank = False)
    nbcoeurcuda = models.IntegerField(blank=False)
    rtxenable = models.BooleanField(blank=False)

    def __str__(self):
        chaine = f"La carte {self.titre} fabriqué en {self.date_sortie} dispose de {self.nbcoeurcuda} coeurs CUDA, de {self.qtevram}Go de VRAM . Elle est destinée au {self.categorie}"
        return chaine