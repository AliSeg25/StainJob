# Generated by Django 4.1.5 on 2023-03-05 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('plateforme', '0010_rename_creuser_adduser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddUser',
            new_name='CustomUser',
        ),
    ]
