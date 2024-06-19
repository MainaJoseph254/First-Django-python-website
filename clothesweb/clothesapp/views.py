from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.
def clothesapp_list(request):
    Posts = Post.objects.all().order_by('-date')
    return render(request,'clothesapp/clothesapp_list.html', {'clothesapp': Posts})
def clothesapp_page(request, slug):
    return HttpResponse(slug)
