from django.urls import path
from . import views

app_name ='blog'
urlpatterns=[
       path("",views.index,name="Index"),
       path("post/<str:slug>",views.details,name="Details"),
       path("New_url_Testing",views.new_url_view,name="New_Url"),
       path("old_url",views.old_url_redirect,name="old_url"),
       path("contact",views.contact_view,name="contact"),
]