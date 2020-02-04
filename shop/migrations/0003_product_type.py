# Generated by Django 2.2.7 on 2020-01-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('X', 'Select type'), ('Dresses', 'Dresses'), ('Bracelets', 'Bracelets')], default='X', max_length=1, null=True),
        ),
    ]