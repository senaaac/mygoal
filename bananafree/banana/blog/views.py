# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def post_list(request):
    # return render(request, 'blog/post_list.html', {})

def index(request):
    return render(request, 'index.html', {})
