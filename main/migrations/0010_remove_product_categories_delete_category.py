# Generated by Django 5.1.1 on 2024-10-01 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
