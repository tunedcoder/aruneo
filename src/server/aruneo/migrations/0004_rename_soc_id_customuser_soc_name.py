# Generated by Django 4.0.3 on 2022-03-29 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aruneo', '0003_customuser_soc_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='soc_id',
            new_name='soc_name',
        ),
    ]
