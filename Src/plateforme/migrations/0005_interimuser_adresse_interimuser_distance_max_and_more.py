# Generated by Django 4.1.5 on 2023-03-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateforme', '0004_interimuser_nom_interimuser_prenom'),
    ]

    operations = [
        migrations.AddField(
            model_name='interimuser',
            name='adresse',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='distance_max',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Distance maximale de déplacement'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interimuser',
            name='telephone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
