# Generated by Django 5.1.4 on 2025-01-11 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_rename_state_listing_is_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
