from blog.models import Post
from django.shortcuts import render_to_response
from bson.objectid import ObjectId

def post_get_all( request ):
    post_list = Post.objects.all()
    # locals() gives us a mapping of symbolic local variable names to
    # their values.
    return render_to_response('post_list.html', locals())

def post_get_one( request ):
    # We need to turn the GET parameter string into an ObjectId
    # object, so we can use it to look up the right Post.
    post = Post.objects.get( pk=ObjectId(request.GET['post_id']) )
    return render_to_response('post_detail.html', locals())
