from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random
class Command(BaseCommand):
    help = "Populate data in the database"

    def handle(self, *args:Any, **options:Any):
        Post.objects.all().delete()
        title=[
    "The Future of AI",
    "Climate Change",
    "The Future of Work",
    "The Future of Education",
    "The Future of Healthcare",
    "Deep Learning and Neural Networks",
    "The Future of Transportation",
    "Medical technology",
    "The Art of cooking",
    "The Future of Space Exploration",
    "The Future of Robotics",
    "Evolution of social media",
    "The Future of Entertainment",
    "Globalization Impact",
    "The Future of Energy",
    "The Future of Money",
    "Online Education",
    "Psychology of Success",
    "Psychology of Decision Making",
    "The Future of Retail",
]

        content=[
    "The future of AI is a hot topic. AI is changing the way we live and work. It is revolutionizing industries and creating new opportunities. In this blog post, we will explore the future of AI and what it means for the world.",
    "Climate change is a pressing issue that affects us all. It is changing the way we live and work. In this blog post, we will explore the impact of climate change and what we can do to address it.",
    "The future of work is changing. With the rise of automation and AI, many jobs are at risk. In this blog post, we will explore the future of work and what it means for the workforce.",
    "The future of education is evolving. With the rise of online learning and AI, education is becoming more accessible. In this blog post, we will explore the future of education and what it means for students.",
    "The future of healthcare is changing. With the rise of medical technology and AI, healthcare is becoming more personalized. In this blog post, we will explore the future of healthcare and what it means for patients.",
    "Deep learning and neural networks are revolutionizing AI. In this blog post, we will explore the impact of deep learning and neural networks on AI and what it means for the future.",
    "The future of transportation is evolving. With the rise of electric vehicles and autonomous cars, transportation is becoming more sustainable. In this blog post, we will explore the future of transportation and what it means for the environment.",
    "Medical technology is changing the way we live and work. In this blog post, we will explore the impact of medical technology on healthcare and what it means for patients.",
    "The art of cooking is a timeless tradition. In this blog post, we will explore the history of cooking and what it means for the future of food.",
    "The future of space exploration is an exciting topic. With the rise of private space companies and new technologies, space exploration is becoming more accessible. In this blog post, we will explore the future of space exploration and what it means for humanity.",
    "The future of robotics is changing the way we live and work. In this blog post, we will explore the impact of robotics on industries and what it means for the future.",
    "The evolution of social media is a fascinating topic. In this blog post, we will explore the history of social media and what it means for the future of communication.",
    "The future of entertainment is evolving. With the rise of streaming services and new technologies, entertainment is becoming more accessible. In this blog post, we will explore the future of entertainment and what it means for the industry.",
    "Globalization has had a profound impact on the world. In this blog post, we will explore the impact of globalization on economies and what it means for the future.",
    "The future of energy is changing. With the rise of renewable energy and new technologies, energy is becoming more sustainable. In this blog post, we will explore the future of energy and what it means for the environment.",
    "The future of money is evolving. With the rise of digital currencies and blockchain technology, money is becoming more decentralized. In this blog post, we will explore the future of money and what it means for the economy.",
    "Online education is changing the way we learn. In this blog post, we will explore the impact of online education on students and what it means for the future of learning.",
    "The psychology of success is a fascinating topic. In this blog post, we will explore the psychology of success and what it means for achieving your goals.",
    "The psychology of decision making is an important topic. In this blog post, we will explore the psychology of decision making and what it means for making better choices.",
    "The future of retail is evolving. With the rise of e-commerce and new technologies, retail is becoming more personalized. In this blog post, we will explore the future of retail and what it means for the industry.",
]

        img_urls=[
   "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400"
]

        categories = Category.objects.all()
        for title, content, img_url in zip(title, content, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url,category=category)

        self.stdout.write(self.style.SUCCESS("Data populated successfully!"))
    