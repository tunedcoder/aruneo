# Generated by Django 4.0.3 on 2022-03-28 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('aruneo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='soc_id',
        ),
        migrations.RemoveField(
            model_name='data',
            name='id',
        ),
        migrations.RemoveField(
            model_name='society',
            name='id',
        ),
        migrations.AddField(
            model_name='data',
            name='data_id',
            field=models.CharField(blank=True, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='data',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='soc_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='aruneo.society'),
        ),
        migrations.AddField(
            model_name='data',
            name='user_associated',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='society',
            name='soc_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='house_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False),
        ),
    ]