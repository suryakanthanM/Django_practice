from django.contrib import admin
from .models import Post, Category, AboutUs


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content') #used to show the search bar
    # list_display = ('title', 'slug', 'content') this line used to show selected fields in admin user page
    list_filter = ('category','created_at')


# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(AboutUs)

