# Generated by Django 3.1.6 on 2021-02-22 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/arrow-up.png', null=True, upload_to=''),
        ),
    ]
