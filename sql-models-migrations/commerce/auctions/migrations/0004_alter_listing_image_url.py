# Generated by Django 5.1.4 on 2025-01-09 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_listing_starting_bid_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.URLField(max_length=256),
        ),
    ]
