# Generated by Django 2.2.7 on 2020-01-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
