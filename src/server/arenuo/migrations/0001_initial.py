# Generated by Django 4.0.3 on 2022-03-22 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_id', models.CharField(max_length=100)),
                ('data_id', models.CharField(max_length=100)),
                ('b_1', models.IntegerField()),
                ('b_2', models.IntegerField()),
                ('b_3', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('uid', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('houses', models.ManyToManyField(related_name='users', to='arenuo.house')),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('houses', models.ManyToManyField(related_name='Houses', to='arenuo.house')),
                ('members', models.ManyToManyField(related_name='members', to='arenuo.user')),
            ],
        ),
    ]