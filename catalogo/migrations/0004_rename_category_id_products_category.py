# Generated by Django 4.2.1 on 2023-06-17 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_products_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category_id',
            new_name='category',
        ),
    ]
