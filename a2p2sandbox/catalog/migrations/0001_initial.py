# Generated by Django 2.1.7 on 2019-03-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_timestamp', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('item_image', models.ImageField(default='images/catalog/default.jpg', upload_to='images/catalog//items_images')),
            ],
        ),
    ]
