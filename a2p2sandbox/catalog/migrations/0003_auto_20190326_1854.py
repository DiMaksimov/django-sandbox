# Generated by Django 2.1.7 on 2019-03-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190326_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogitem',
            name='item_image',
            field=models.ImageField(default='images/catalog/default.jpg', upload_to='images/catalog/items_images'),
        ),
    ]
