from django.conf.urls import patterns, include, url
from .views import UserProfileRetrieveAPIView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'discussion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^user-profile/', UserProfileRetrieveAPIView.as_view()),
)
