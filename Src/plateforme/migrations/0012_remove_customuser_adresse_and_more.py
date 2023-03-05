# Generated by Django 4.1.5 on 2023-03-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('plateforme', '0011_rename_adduser_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='employeur',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='interimaire',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='nom_complet',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='numero_de_telephone',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='pays',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='ville',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', to='auth.permission', verbose_name='user permissions'),
        ),
    ]