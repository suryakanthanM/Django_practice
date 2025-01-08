from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populate category data in the database"

    def handle(self, *args:Any, **options:Any):
        Category.objects.all().delete()
        categories = ["Technology", "Health", "Education", "Science", "Entertainment", "Business", "Travel", "Food", "Fashion", "Sports"]

        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Data populated successfully!"))
    