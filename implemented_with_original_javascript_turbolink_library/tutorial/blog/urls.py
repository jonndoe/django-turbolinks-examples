from django.conf.urls import url
from django.views.generic import ListView, DateDetailView
from blog.views import PostListView, PostDetailView

from blog.models import Post


app_name = 'blog'


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        PostDetailView.as_view(),
        name='post-detail')
]
