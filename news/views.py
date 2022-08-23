from django.shortcuts import render
from news.models import News


def index(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "news/index.html", context)
