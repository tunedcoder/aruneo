# Generated by Django 4.0.3 on 2022-03-24 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aruneo', '0002_society_customuser_user_id_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='user_assocaited',
            new_name='user_associated',
        ),
    ]