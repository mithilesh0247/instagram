# Generated by Django 3.2.14 on 2022-08-27 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Influencer', '0007_influencerstory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='influencerstory',
            old_name='field_name',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='influencerstory',
            old_name='user_id',
            new_name='user_type',
        ),
    ]