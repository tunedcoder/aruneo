# Generated by Django 4.0.3 on 2022-03-29 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aruneo', '0004_rename_soc_id_customuser_soc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='bucket_1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='data',
            name='bucket_2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='data',
            name='bucket_3',
            field=models.FloatField(default=0),
        ),
    ]
