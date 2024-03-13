# Generated by Django 4.1 on 2022-09-25 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_rename_cus_name_contactus_nameofcus'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GS_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('Category', models.CharField(choices=[('Cement', 'cement'), ('steel', 'steel'), ('Sand', 'sand'), ('bricks', 'bricks'), ('crush', 'crush'), ('other_const', 'other_const')], max_length=30)),
                ('prod_img', models.ImageField(upload_to='GSproductimg')),
            ],
        ),
        migrations.CreateModel(
            name='orderplaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=5)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Acepted', 'Acepted'), ('packed', 'packed'), ('On the way', 'On the way'), ('Deliverd', 'Deliverd'), ('Cancal', 'Cancal')], default='pending', max_length=50)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
                ('gs_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.gs_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=5)),
                ('gs_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.gs_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
