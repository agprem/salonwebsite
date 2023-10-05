# Generated by Django 3.2.5 on 2021-09-24 10:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='alltimeoffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offercategory', models.CharField(blank=True, default='All Time Offers', max_length=100)),
                ('offername', models.CharField(max_length=30)),
                ('offerdetail', models.TextField(blank=True, max_length=200)),
                ('offerimg', models.ImageField(default='default.jpg', upload_to='offer_pics')),
                ('offerexp', models.DateField(default=datetime.date(2021, 11, 23))),
                ('price', models.IntegerField(blank=True)),
                ('discount', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='discountoffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offercategory', models.CharField(blank=True, default='Discount Offers', max_length=100)),
                ('offername', models.CharField(max_length=30)),
                ('offerdetail', models.TextField(blank=True, max_length=200)),
                ('offerimg', models.ImageField(default='default.jpg', upload_to='offer_pics')),
                ('offerexp', models.DateField(default=datetime.date(2021, 11, 23))),
                ('price', models.IntegerField(blank=True)),
                ('discount', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='otheroffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offercategory', models.CharField(blank=True, default='Other Offers', max_length=100)),
                ('offername', models.CharField(max_length=30)),
                ('offerdetail', models.TextField(blank=True, max_length=200)),
                ('offerimg', models.ImageField(default='default.jpg', upload_to='offer_pics')),
                ('offerexp', models.DateField(default=datetime.date(2021, 11, 23))),
                ('price', models.IntegerField(blank=True)),
                ('discount', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('productdetail', models.CharField(blank=True, max_length=200)),
                ('productimg', models.ImageField(default='default.jpg', upload_to='product_pics')),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('discount', models.IntegerField(blank=True, default=0)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='seasonaloffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offercategory', models.CharField(blank=True, default='Seasonal Offers', max_length=100)),
                ('offername', models.CharField(max_length=30)),
                ('offerdetail', models.TextField(blank=True, max_length=200)),
                ('offerimg', models.ImageField(default='default.jpg', upload_to='offer_pics')),
                ('offerexp', models.DateField(default=datetime.date(2021, 11, 23))),
                ('price', models.IntegerField(blank=True)),
                ('discount', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=0)),
                ('cartitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdate', models.DateTimeField(blank=True, null=True)),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='salon.CartItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='bookappointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=20, verbose_name='Service/Package')),
                ('technician', models.CharField(max_length=20, verbose_name='Technician')),
                ('date', models.DateField(blank=True, default=datetime.date(2021, 9, 24), null=True)),
                ('time', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('aptdone', models.BooleanField(default=False)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
