# Generated by Django 4.2.16 on 2025-02-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_product_email_product_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('shipping_address', models.TextField()),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
        migrations.RemoveField(
            model_name='product',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='product',
            name='shipping_address',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(),
        ),
    ]
