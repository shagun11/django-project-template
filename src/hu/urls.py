from django.conf.urls import patterns, include, url
from hu import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hu.views.home', name='home'),
    url(r'^tasks/$','hu.views.get_tasks',name='get_tasks'),
    url(r'^tasks/pending$', 'hu.views.tasks_pending'),
    url(r'^details/', 'hu.views.get_details',name='movie_detail'),
    url(r'^search/', 'hu.views.search',name='search')
    
)






