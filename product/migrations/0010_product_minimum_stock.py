# Generated by Django 4.0.6 on 2024-06-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_discount_exempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='minimum_stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
