# Generated by Django 5.0.7 on 2025-04-07 19:00

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_email', models.TextField(blank=True, null=True, verbose_name='email address')),
                ('phone', models.TextField(blank=True, max_length=16, null=True)),
                ('address', models.TextField(blank=True, help_text='', max_length=2555, null=True)),
                ('ordered_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=355, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product Specification',
                'verbose_name_plural': 'Product Specifications',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Required', max_length=355, verbose_name='Product Name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Product Type',
                'verbose_name_plural': 'Product Types',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(help_text='Required', max_length=250, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=250, primary_key=True, serialize=False, unique=True, verbose_name='Category URL')),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Products.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.TextField(help_text='Required', max_length=355, null=True, verbose_name='Product Name')),
                ('description', models.TextField(blank=True, help_text='Required', max_length=355, verbose_name='Description')),
                ('slug', models.SlugField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('regular_price', models.DecimalField(decimal_places=1, error_messages={'name': {'max_length': 'The price must be between 0 and 99999.9'}}, help_text='Maximum 99999.9', max_digits=7, verbose_name='Regular Price')),
                ('discount_price', models.DecimalField(decimal_places=1, error_messages={'name': {'max_length': 'The price must be between 0 and 99999.9'}}, help_text='Maximum 99999.9', max_digits=7, verbose_name='Discount Price')),
                ('image', models.ImageField(blank=True, help_text='upload image', null=True, upload_to='images/', verbose_name='image1')),
                ('image_first', models.ImageField(blank=True, help_text='upload image', null=True, upload_to='images/', verbose_name='image2')),
                ('image_second', models.ImageField(blank=True, help_text='upload image', null=True, upload_to='images/', verbose_name='image3')),
                ('image_third', models.ImageField(blank=True, help_text='upload image', null=True, upload_to='images/', verbose_name='image4')),
                ('is_active', models.BooleanField(default=True, help_text='Set Product Visibility', verbose_name='Product Visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Products.category')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Products.producttype')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=100)),
                ('total_price', models.DecimalField(decimal_places=1, max_digits=7)),
                ('ordered_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecificationValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(help_text='Maximum of 200 characters', max_length=200, verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Products.productspecification')),
            ],
            options={
                'verbose_name': 'Product Specification Value',
                'verbose_name_plural': 'Product Specification Values',
            },
        ),
        migrations.AddField(
            model_name='productspecification',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Products.producttype'),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
