# Generated by Django 4.1.3 on 2022-12-18 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customers',
            new_name='customer',
        ),
    ]
