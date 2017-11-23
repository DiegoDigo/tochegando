from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^drivers/?$', views.Drivers.as_view()),
    url(r'^drivers/(?P<pk>\d+)?$', views.DriversByID.as_view()),
    url(r'^vehicles/(?P<pk>\d+)/?$', views.Vehicles.as_view()),
]