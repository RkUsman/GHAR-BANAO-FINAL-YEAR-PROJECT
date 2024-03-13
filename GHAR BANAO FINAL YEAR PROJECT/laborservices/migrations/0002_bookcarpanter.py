# Generated by Django 4.1 on 2022-09-25 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laborservices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookCarpanter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('Customer_name', models.CharField(max_length=20)),
                ('HomeAddress', models.CharField(max_length=90)),
                ('payment_mode', models.CharField(max_length=40)),
                ('carpen_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laborservices.carpanter')),
            ],
        ),
    ]
