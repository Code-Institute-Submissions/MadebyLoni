# Generated by Django 2.2.7 on 2020-01-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0005_wishlist_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]