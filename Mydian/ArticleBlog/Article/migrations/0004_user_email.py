# Generated by Django 2.1.8 on 2019-09-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]