# Generated by Django 4.2.6 on 2023-12-08 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_discount_price_product_discounted_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
    ]
