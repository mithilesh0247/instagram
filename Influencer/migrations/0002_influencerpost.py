# Generated by Django 3.2.14 on 2022-08-06 13:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Influencer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfluencerPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=500)),
                ('file', models.ImageField(blank=True, null=True, upload_to='postimage/')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('add_external_links', models.CharField(max_length=500)),
                ('tag', models.CharField(max_length=200)),
                ('post_type', models.CharField(blank=True, choices=[('collaboration', 'collaboration'), ('paid promotion', 'paid promotion'), ('normal', 'normal')], default='normal', max_length=100, null=True)),
                ('collaboration_with', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('companion_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sender', models.CharField(max_length=100)),
            ],
        ),
    ]