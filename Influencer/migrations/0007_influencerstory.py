# Generated by Django 3.2.14 on 2022-08-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Influencer', '0006_alter_influencer_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfluencerStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='storyimage/')),
                ('field_name', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
