# Generated by Django 3.2.14 on 2022-08-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Influencer', '0004_influencer_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='date_of_birth',
            field=models.DateField(blank=True, max_length=25, null=True),
        ),
    ]
