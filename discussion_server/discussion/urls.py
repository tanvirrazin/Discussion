from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'discussion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/', include('api.urls')),
)
