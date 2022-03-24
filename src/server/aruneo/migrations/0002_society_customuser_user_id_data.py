# Generated by Django 4.0.3 on 2022-03-24 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aruneo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('transmitter_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bucket_1', models.IntegerField(default=0)),
                ('bucket_2', models.IntegerField(default=0)),
                ('bucket_3', models.IntegerField(default=0)),
                ('soc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aruneo.society')),
                ('user_assocaited', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
