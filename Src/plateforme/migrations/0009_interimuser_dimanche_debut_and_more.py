# Generated by Django 4.1.5 on 2023-03-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateforme', '0008_empuser_domaine'),
    ]

    operations = [
        migrations.AddField(
            model_name='interimuser',
            name='dimanche_debut',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='dimanche_dispo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='dimanche_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='jeudi_debut',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='jeudi_dispo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='jeudi_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='lundi_debut',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='lundi_dispo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='lundi_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='mardi_debut',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='mardi_dispo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='mardi_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='mercredi_debut',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='mercredi_dispo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='mercredi_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='samedi_debut',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='samedi_dispo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='samedi_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='vendredi_debut',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='vendredi_dispo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interimuser',
            name='vendredi_fin',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
