from django.db import models



class Project(models.Model):
    name = models.CharField(max_length=20)
    ladate = models.DateField()
    description = models.TextField()
    categorie = models.CharField(max_length=100, choices=[  # Catégorie du projet
        ('dev', 'Développement'),
        ('design', 'Design'),
        ('cyber', 'Cybersécurité'),
        ('art', 'Artistique'),
        ('crea', 'Création de contenu'),
        ('entr', 'Entreprenariat'),
        ('autre', 'Autre')],
        default = 'autre' )
    def __str__(self):
        return self.name
# Create your models here.
