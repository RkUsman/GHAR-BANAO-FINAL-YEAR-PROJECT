# Generated by Django 4.1 on 2022-09-21 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='cus_name',
            new_name='nameofcus',
        ),
    ]
