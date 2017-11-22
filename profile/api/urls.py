from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^parents/?$', views.Parents.as_view(), name='parent'),
    url(r'^children/?$', views.Children.as_view(), name='child'),
    url(r'^schools/?$', views.Schools.as_view(), name="school"),
]