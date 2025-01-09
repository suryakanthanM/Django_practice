from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
# posts=[
#         {'id':1,"title": "Post 1", "content": "content of 1"},
#         {'id':2,"title": "Post 2", "content": "content of 2"},
#         {'id':3,"title": "Post 3", "content": "content of 3"},
#         {'id':4,"title": "Post 4", "content": "content of 4"},
#     ]
def index(request):
    blog_title ="Latest Posts"
     
    search= request.GET.get('q','')

    if search:
       all_posts = Post.objects.filter(title__icontains = search)
    else:
       all_posts = Post.objects.all()

    
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'blog_title':blog_title, 'page_obj':page_obj, 'search':search})

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
    if request.method == 'POST':
       form = ContactForm(request.POST)
       name = request.POST.get('name')
       email = request.POST.get('email')
       message = request.POST.get('message')

       logger = logging.getLogger("testing")
       if form.is_valid():
           logger.debug(f'Post Data: {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')

        #    admin_email = 'solohero300@gmail.com'
        #    subject = f"New contact From Submission from {name}"
        #    email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        #    send_mail(subject,email_message,settings.DEFAULT_FROM_EMAIL,[admin_email],fail_silently=False)

           success_message = 'Your Email has been sent!'
           return render(request,'contact.html',{'form':form, 'success_message':success_message})

       else:
           logger.debug(f'Form is not valid')
       return render(request,'contact.html',{'form':form, 'name':name, 'email':email, 'message':message})
    return render(request,'contact.html')

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,'about.html',{'about_content':about_content})

