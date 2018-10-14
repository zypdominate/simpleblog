from django.conf.urls import  include,url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail,name='detail'),  # http://127.0.0.1:8000/post/1/
]