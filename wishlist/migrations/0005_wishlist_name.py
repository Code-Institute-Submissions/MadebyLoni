# Generated by Django 2.2.7 on 2020-01-27 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0004_remove_wishlist_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]