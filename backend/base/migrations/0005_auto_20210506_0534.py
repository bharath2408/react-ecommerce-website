# Generated by Django 3.1.4 on 2021-05-06 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210503_0824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='deliverdAt',
            new_name='delivereddAt',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='isDeliverd',
            new_name='isDelivered',
        ),
    ]
