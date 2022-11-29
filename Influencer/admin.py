from django.contrib import admin
from Influencer.models import Influencer, InfluencerPost, InfluencerStory


class InfluencerAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "date_of_birth", "city", "state", "country", "platform", "other",
                    "region_of_influence", "monetizing_audience", "monthly_earnings", "audience", "audience_age_range", "main_content_category", "follow"]


admin.site.register(Influencer, InfluencerAdmin)


class InfluencerPostAdmin(admin.ModelAdmin):
    list_display = ["post_type_id", "msg", "file", "video", "add_external_links", "tag",
                    "post_type", "collaboration_with", "location", "companion_name", "created_at", "sender"]


admin.site.register(InfluencerPost, InfluencerPostAdmin)


class InfluencerStoryAdmin(admin.ModelAdmin):
    list_display = ['user_type', 'image']


admin.site.register(InfluencerStory, InfluencerStoryAdmin)
