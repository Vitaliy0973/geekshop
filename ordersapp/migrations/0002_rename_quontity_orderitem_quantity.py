# Generated by Django 3.2.6 on 2022-05-04 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quontity',
            new_name='quantity',
        ),
    ]
