# Generated by Django 3.0.6 on 2020-07-06 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('postal_code', models.CharField(max_length=100, null=True)),
                ('other', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('tag', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_no', models.CharField(max_length=100, null=True)),
                ('cc_expiry', models.DateField()),
                ('cc_code', models.CharField(max_length=100, null=True)),
                ('billing_address', models.CharField(max_length=200, null=True)),
                ('customerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_manag_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(null=True)),
                ('quantity', models.IntegerField()),
                ('productID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_manag_app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out of delivery'), ('Delivered', 'Delivered')], max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_manag_app.Customer')),
                ('order_productID', models.ManyToManyField(to='shop_manag_app.Order_Product')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='delivery_address',
            field=models.ManyToManyField(to='shop_manag_app.Delivery_Address'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
