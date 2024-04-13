from django.shortcuts import render
def home(request):
    return render(request,"blog/home.html")
def register(request):
    return render(request,"blog/register.html")
def login(request):
    return render(request,"blog/login.html")
def logout(request):
    return render(request,"blog/home.html")
def detailsBlog(request):
    return render(request,"blog/blog-detail.html")
def listBlog(request):
    return render(request,"blog/list-blog.html")
def contact(request):
    return render(request,"blog/contact.html")
# Create your views here.
