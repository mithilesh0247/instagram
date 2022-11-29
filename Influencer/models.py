from datetime import datetime
from email.policy import default
from django.db import models
from sqlalchemy import ForeignKey
from account.models import User
from django.core.validators import FileExtensionValidator
from django_mysql.models import ListCharField
from django.db.models import CharField, Model
# Create your models here.


class Influencer(models.Model):
    # influencer_mob = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    # influencer_id=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=25, null=True, blank=True)
    city = models.CharField(max_length=50)
    STATE_CHOICES = (
        ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
        ('Daman and Diu', 'Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu & Kashmir', 'Jammu & Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttarakhand', 'Uttarakhand'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('West Bengal', 'West Bengal'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    country = models.CharField(max_length=50)
    PLATFORM_CHOICES = (
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('Youtube', 'Youtube'),
        ('Pinterest', 'Pinterest'),
        ('Linkedin', 'Linkedin'),
        ('Pinterest', 'Pinterest'),
        ('Twitter', 'Twitter'),

    )
    platform = models.CharField(choices=PLATFORM_CHOICES, max_length=50)
    other = models.CharField(max_length=50)
    region_of_influence = models.CharField(
        choices=STATE_CHOICES, max_length=70)
    MONETIZING_AUDIENCE_CHOICES = (
        ('Sponsered Blog Posts', 'Sponsered Blog Posts'),
        ('Sponsered Social media Posts', 'Sponsered Social media Posts'),
        ('Cost Per Action Ads', 'Cost Per Action Ads'),
        ('Cost Per Click Ads', 'Cost Per Click Ads'),
        ('Affiliate Programs', 'Affiliate Progams'),
        ('Not Currently Monetizing', 'Not  Currently Monetizing'),
    )
    monetizing_audience = models.CharField(
        choices=MONETIZING_AUDIENCE_CHOICES, max_length=100)
    monthly_earnings = models.FloatField(null=True, blank=True, default=False)
    AUDIENCE_CHOICES = (
        ('Gender(mainly)', 'Gender(mainly)'),
        ('Female', 'Femal'),
        ('Others', "Others"),
        ('All', 'All'),
    )
    audience = models.CharField(choices=AUDIENCE_CHOICES, max_length=14)
    AUDIENCE_AGE_RANGE_CHOICES = (
        ('Gen Z(10-25)', 'Gen Z(10-25)'),
        ('Millennials(26-41)', 'Millennnials(26-41)'),
        ('Gen X(42-57)', 'Gen X(42-57)'),
        ('Boomers II(58-67)', 'Boomers II(58-67)'),
    )
    audience_age_range = models.CharField(
        choices=AUDIENCE_AGE_RANGE_CHOICES, max_length=100)
    CONTENT_CATEGORY = (
        ('Fashion', 'Fashion'),
        ('Lifestyle', 'Lifestyle'),
        ('DIY', 'DIY'),
        ('Entertainment', 'Entertainment'),
        ('Travel', 'Travel'),
        ('Music', 'Music'),
        ('Business', 'Business'),
        ('Beauty', 'Beauty'),
        ('Education', 'Education'),
        ('Health and Fitness', 'Health and Fitness'),
        ('Photography', 'Photography'),
        ('other', 'other'),
    )

    main_content_category = models.CharField(
        choices=CONTENT_CATEGORY, max_length=100)
    follow = ListCharField(
        base_field=CharField(max_length=10),
        default=None,
        null=True,
        size=6,
        max_length=(6 * 11),  # 6 * 10 character nominals, plus commas
    )


class InfluencerPost(models.Model):
    post_type_id = models.IntegerField(default=None)
    msg = models.CharField(max_length=500)
    file = models.ImageField(
        upload_to="postimage/", blank=True, null=True)
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    add_external_links = models.CharField(max_length=500)
    tag = models.CharField(max_length=200)
    POST_CHOICE = (
        ('collaboration', 'collaboration'),
        ('paid promotion', 'paid promotion'),
        ('normal', 'normal'),
    )
    post_type = models.CharField(
        default='normal', max_length=100, choices=POST_CHOICE, blank=True, null=True)

    collaboration_with = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    companion_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=100)


class InfluencerStory(models.Model):
    user_type = models.IntegerField(null=True, blank=True)
    image = models.ImageField(
        upload_to="influencerstoryimage/", blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
