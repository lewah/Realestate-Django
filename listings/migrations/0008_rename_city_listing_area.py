# Generated by Django 3.2.4 on 2021-06-25 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_listing_county'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='city',
            new_name='area',
        ),
    ]
