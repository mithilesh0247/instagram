from django.urls import path
from company.views import BrandRegistration, BrandProfileView, BrandProfileUpdateView, InfluencerMessageView, BrandMessageView, BrandPost
urlpatterns = [
    path('register/', BrandRegistration.as_view(), name='register'),
    path('profile/', BrandProfileView.as_view(), name='profile'),
    path("update/", BrandProfileUpdateView.as_view(), name='update'),
    path("influencermessage/", InfluencerMessageView.as_view(),
         name='influencermessage'),
    path("brandmessage/", BrandMessageView.as_view(), name='brandmessage'),
    path("brandpost/", BrandPost.as_view(), name='brandpost'),
]
