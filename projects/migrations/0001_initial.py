# Generated by Django 4.2.19 on 2025-02-21 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ladate', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('categorie', models.CharField(choices=[('dev', 'Développement'), ('design', 'Design'), ('cyber', 'Cybersécurité'), ('art', 'Artistique'), ('crea', 'Création de contenu'), ('entr', 'Entreprenariat'), ('autre', 'Autre')], default='autre', max_length=100)),
            ],
        ),
    ]
