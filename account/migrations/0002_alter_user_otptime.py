# Generated by Django 3.2.14 on 2022-08-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otptime',
            field=models.CharField(default='181913', max_length=100),
        ),
    ]
