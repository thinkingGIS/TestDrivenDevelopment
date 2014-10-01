from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'superlist.views.home', name='home'),
    url(r'^(\d+)/$', 'lists.views.view_list',
        name='view_list'
        ),
    # url(r'^(\d+)/add_item$', 'lists.views.add_item',
    #     name='add_item'
    #     ),
    url(r'^new$', 'lists.views.new_list',
        name='new_list'
        ),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
