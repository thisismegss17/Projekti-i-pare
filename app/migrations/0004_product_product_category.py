# Generated by Django 5.0.7 on 2024-07-11 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_kategori_kategori_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.kategori'),
        ),
    ]
