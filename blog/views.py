from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
# Create your views here.
# posts=[
#         {'id':1,"title": "Post 1", "content": "content of 1"},
#         {'id':2,"title": "Post 2", "content": "content of 2"},
#         {'id':3,"title": "Post 3", "content": "content of 3"},
#         {'id':4,"title": "Post 4", "content": "content of 4"},
#     ]
def index(request):
    blog_title ="Latest Posts"

    all_posts = Post.objects.all()
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'blog_title':blog_title, 'page_obj':page_obj})

def details(request,slug):
    #static data
    # post = next((item for item in posts if item["id"] == int(post_id)), None)
    #dynamic data by using post id
    try:
        post = Post.objects.get(slug=slug) 
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        return Http404("Post does not exist") 
    # logger = logging.getLogger("testing")
    # logger.debug(f'Post requested: {post}')
    return render(request,'detail.html',{'post':post, 'related_posts':related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:New_Url'))

def new_url_view(request):
    return HttpResponse("This is the new url view")

def contact_view(request):
    return render(request,'contact.html')

