# team_management/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include your app's URLs
    path('team/', include('team_management_app.urls')),
    # You can include other apps' URLs as needed
]
