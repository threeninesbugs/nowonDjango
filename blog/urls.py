from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/test/$', views.post_test, name='post_test'),
    url(r'^post/connect$', views.post_write, name='post_write'),
    url(r'^post/result.html$', views.post_result, name='post_result'),
]