from django.contrib import admin
from company.models import Brand, MessageInfluencer, MessageBrand, BrandPost
# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'designation', 'proof_of_employement', 'brand_name', 'company_website',
                    'brand_logo', 'industry', 'company_type', 'company_size', 'select_document', 'upload_document']


admin.site.register(Brand, BrandAdmin)


class MessageInfluencerAdmin(admin.ModelAdmin):
    list_display = ['msg', 'date', 'file', 'sender']


admin.site.register(MessageInfluencer, MessageInfluencerAdmin)


class MessageBrandAdmin(admin.ModelAdmin):
    list_display = ['msg', 'date', 'file', 'sender']


admin.site.register(MessageBrand, MessageBrandAdmin)


class BrandPostAdmin(admin.ModelAdmin):
    list_display = ["msg", "file", "video", "add_external_links", "tag",
                    "post_type", "collaboration_with", "location", "companion_name", "created_at", "sender"]


admin.site.register(BrandPost, BrandPostAdmin)
