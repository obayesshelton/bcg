from django.conf.urls import url
from bcg_image import views

urlpatterns = [
  url(r'^upload/$', views.image_list),
  url(r'^upload/(?P<extension>.+)/$', views.image_list),
  url(r'^upload/(?P<id>[0-9]+)$', views.image_detail),
]
