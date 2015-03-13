from django.conf.urls import patterns, include, url
from api.views import *
from contacts.views import SignupView, UserListCreateAPIView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'discussion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', LoginView.as_view()),
    url(r'^logout/', LogoutView.as_view()),
    url(r'^signup/', SignupView.as_view()),
    url(r'^friends/', UserListCreateAPIView.as_view()),
)
