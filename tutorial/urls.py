from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url( r'^$', 'blog.views.post_get_all', name='post_get_all' ),
                       url( r'^posts/$', 'blog.views.post_get_one', name='post_get_one' ),
)
