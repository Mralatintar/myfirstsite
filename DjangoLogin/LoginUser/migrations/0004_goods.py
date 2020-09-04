# Generated by Django 2.1.8 on 2019-09-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0003_auto_20190904_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_number', models.CharField(max_length=11)),
                ('goods_name', models.CharField(max_length=32)),
                ('goods_location', models.CharField(max_length=254)),
                ('goods_price', models.FloatField()),
                ('goods_pro_time', models.DateField(auto_now=True)),
                ('goods_safe_date', models.IntegerField()),
                ('goods_count', models.IntegerField()),
            ],
        ),
    ]