# Generated by Django 3.2.14 on 2022-08-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_alter_user_otptime'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='emailotp',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='emailotptime',
            field=models.CharField(default='144945', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='otptime',
            field=models.CharField(default='144945', max_length=100),
        ),
    ]