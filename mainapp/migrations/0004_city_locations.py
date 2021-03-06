# Generated by Django 3.2.7 on 2021-10-09 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, verbose_name='номер телефона')),
                ('email', models.CharField(max_length=60, verbose_name='Email')),
                ('address', models.CharField(max_length=100, verbose_name='адрес')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.city')),
            ],
        ),
    ]
