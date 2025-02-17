# Generated by Django 4.2.16 on 2025-02-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default='YYYY-MM-DD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.DecimalField(decimal_places=2, default='3', max_digits=10),
            preserve_default=False,
        ),
    ]
