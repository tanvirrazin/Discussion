from django.conf.urls import patterns, include, url
from .views import TopicListCreateAPIView, TopicLikeDislikeAPIView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'discussion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^topics/', TopicListCreateAPIView.as_view()),
    url(r'^like-topic/(?P<pk>[0-9]+)/', TopicLikeDislikeAPIView.as_view()),
)
