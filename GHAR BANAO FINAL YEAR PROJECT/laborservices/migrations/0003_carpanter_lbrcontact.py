# Generated by Django 4.1 on 2022-09-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laborservices', '0002_bookcarpanter'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpanter',
            name='lbrcontact',
            field=models.CharField(default=None, max_length=11),
        ),
    ]
