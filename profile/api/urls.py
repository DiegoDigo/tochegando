from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^parents/$', views.Parents.as_view()),
    url(r'^children/$', views.Children.as_view()),
]