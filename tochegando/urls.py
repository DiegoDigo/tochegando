from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('profile.api.urls', namespace='api')),
    url(r'^', include('vehicle.api.urls')),
]
