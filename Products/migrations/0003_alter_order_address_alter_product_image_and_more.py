# Generated by Django 5.0.7 on 2025-05-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_order_address_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, help_text='', max_length=2555, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='upload image', null=True, upload_to='images/', verbose_name='image1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_first',
            field=models.ImageField(blank=True, help_text='upload image', null=True, upload_to='images/', verbose_name='image2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_second',
            field=models.ImageField(blank=True, help_text='upload image', null=True, upload_to='images/', verbose_name='image3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_third',
            field=models.ImageField(blank=True, help_text='upload image', null=True, upload_to='images/', verbose_name='image4'),
        ),
    ]
