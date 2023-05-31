from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from . import models

class CGForm(ModelForm):
    class Meta :
        model = models.CarteGraphique
        fields = ('nommodel', 'categorie', 'date_sortie', 'qtevram', 'nbcoeurcuda', 'rtxenable')
        labels = {
            'nommodel' : _('Modèle'),
            'categorie' : _('Catégorie'),
            'date_sortie' : _('Date de sortie')
            'qtevram' : _('Quantité de VRAM en Giga')#https://youtu.be/2hsKvZTV7vI?list=PLLQ8NqH1r6GNUbR_D5BkBJbLOmTkFy6tn&t=432
            'nbcoeurcuda' _('Nombre de coeurs CUDA')
            'rtxenable' _('Posède le RTX?')
        }