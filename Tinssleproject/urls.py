from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from account import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('api/influencer/', include('Influencer.urls')),
    path('api/brand/', include('company.urls')),
    #path('api/influencer/', include('post.urls')),
    path('social/', include('account.urls')),
]
