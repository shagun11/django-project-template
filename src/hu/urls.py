from django.conf.urls import patterns, include, url
from hu import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hu.views.home', name='home'),
    url(r'^alltasks/','hu.views.get_tasks',name='get_tasks')
    
)






