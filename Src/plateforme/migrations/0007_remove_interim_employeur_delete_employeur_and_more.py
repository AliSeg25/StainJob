# Generated by Django 4.1.5 on 2023-03-05 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plateforme', '0006_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interim',
            name='Employeur',
        ),
        migrations.DeleteModel(
            name='Employeur',
        ),
        migrations.DeleteModel(
            name='Interim',
        ),
    ]