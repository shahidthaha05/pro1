# Generated by Django 5.1.5 on 2025-02-05 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_cart_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
