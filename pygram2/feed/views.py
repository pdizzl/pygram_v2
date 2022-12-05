from django.shortcuts import render


def home(request):
    return render(request, 'feed.html', {})

def feed(request):
    return render(request, 'feed.html', {})