# Generated by Django 4.0.3 on 2022-04-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aruneo', '0006_rename_date_data_date_enter'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Average_Footprint',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Bio_energyshare',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Credits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Total_Bio_Energy',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Total_Blue_Waste',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Total_Green_Waste',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Total_Red_Waste',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Total_Waste',
            field=models.FloatField(default=0),
        ),
    ]
