from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact, Creative, Vblog, blog

def index(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        return redirect('my_index')
    return render(request, 'index.html')

def services(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        return redirect('my_services')
    return render(request, 'services.html')

def member_blog(request, name):
    creative, created = Creative.objects.get_or_create(name__iexact=name, defaults={'name': name, 'display_name': name.capitalize(), 'role': 'Team Member', 'profile_image_filename': 'default.jpg', 'bio': 'Bio pending.'})
    return render(request, 'member_blog.html', {'display_name': creative.display_name, 'role': creative.role, 'color': creative.color, 'image_path': f"images/{creative.profile_image_filename}", 'bio': creative.bio})

def blogs(request):
    return render(request, 'blogs.html', {'posts': blog.objects.all()})

def vblog(request):
    if not Vblog.objects.exists(): Vblog.objects.create(heading="Sample Video Blog", description="Description pending.")
    return render(request, 'vblog.html', {'blogs': Vblog.objects.all()})

def blog_list(request):
    if not blog.objects.exists(): blog.objects.create(main_title="Sample Blog", author="Admin", sub_heading="First Post")
    return render(request, 'blogs.html', {'posts': blog.objects.all()})

def blog_detail(request, pk):
    post, created = blog.objects.get_or_create(pk=pk, defaults={'main_title': f"Blog {pk}", 'author': 'Admin', 'sub_heading': 'Details pending'})
    return render(request, 'blogs.html', {'post': post})