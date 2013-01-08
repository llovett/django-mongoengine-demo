from blog.models import Post
from django.shortcuts import render_to_response
from bson.objectid import ObjectId

def post_get_all( request ):
    post_list = Post.objects.all()
    return render_to_response('post_list.html', locals())

def post_get_one( request ):
    post = Post.objects.get( pk=ObjectId(request.GET['post_id']) )
    return render_to_response('post_detail.html', locals())
