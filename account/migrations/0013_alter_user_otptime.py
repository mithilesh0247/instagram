# Generated by Django 3.2.14 on 2022-08-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_user_otptime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otptime',
            field=models.CharField(default='140535', max_length=100),
        ),
    ]
