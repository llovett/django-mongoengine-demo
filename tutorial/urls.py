from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Shows all the posts
                       url( r'^$', 'blog.views.post_get_all', name='post_get_all' ),
                       # Shows one post
                       url( r'^posts/$', 'blog.views.post_get_one', name='post_get_one' ),
)
