# Generated by Django 3.1.4 on 2021-05-06 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210506_0534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivereddAt',
            new_name='deliveredAt',
        ),
    ]
