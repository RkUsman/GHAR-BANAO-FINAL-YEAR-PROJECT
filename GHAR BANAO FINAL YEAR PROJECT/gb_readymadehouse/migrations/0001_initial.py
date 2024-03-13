# Generated by Django 3.0.5 on 2022-08-24 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='houseownerdetail',
            fields=[
                ('propertyNum', models.IntegerField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=50)),
                ('phoneNumber', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='readymadehouseimg/')),
                ('house_price', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('date_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='readyhouseimggallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='readymadehouseimg/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gb_readymadehouse.houseownerdetail')),
            ],
        ),
    ]
