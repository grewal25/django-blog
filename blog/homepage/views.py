from django.shortcuts import render

def index(request):
    return render(request, 'homepage/index.html',context=None)


def newsFeed(request):
    return render(request, 'homepage/news_feed.html',context=None)
    
