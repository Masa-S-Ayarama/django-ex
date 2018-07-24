from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', index),
    # url(r'^health$', health),

    # url(r'^blog/', include('blog.urls')),    # blog app
    # url(r'^polls/', include('polls.urls')),  # django tutorial
    url(r'^$', include('home.urls')), 
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
