from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    blog_title ="Latest Posts"
    posts=[
        {'id':1,"title": "Post 1", "content": "content of 1"},
        {'id':2,"title": "Post 2", "content": "content of 2"},
        {'id':3,"title": "Post 3", "content": "content of 3"},
        {'id':4,"title": "Post 4", "content": "content of 4"},
    ]
    return render(request,'index.html',{'blog_title':blog_title,'posts':posts})

def details(request,post_id):
    return render(request,'detail.html')

def old_url_redirect(request):
    return redirect(reverse('blog:New_Url'))

def new_url_view(request):
    return HttpResponse("This is the new url view")