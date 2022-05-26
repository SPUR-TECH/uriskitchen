# Generated by Django 3.2 on 2022-05-26 10:21

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thai', '0002_success'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price_Medium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_Large', models.DecimalField(decimal_places=2, max_digits=5)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('catagory', models.ManyToManyField(related_name='item', to='thai.Catagory')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price_Medium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_Large', models.DecimalField(decimal_places=2, max_digits=5)),
                ('items', models.ManyToManyField(blank=True, related_name='order', to='thai.MenuItem')),
            ],
        ),
        migrations.DeleteModel(
            name='Dessert',
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
        migrations.DeleteModel(
            name='Success',
        ),
    ]