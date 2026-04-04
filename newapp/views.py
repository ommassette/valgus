from django.shortcuts import render, redirect
from .models import Contact
from .models import Creative


def index(request):
    return render(request,'index.html')
def services(request):
    return render(request,'services.html')
def vblog(request):
    return render(request,'vblog.html')
def blogs(request):
    return render(request,'blogs.html')

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


def vblog(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        return redirect('my_vblog') 
    return render(request, 'vblog.html')

def member_blog(request, name):
    from django.shortcuts import get_object_or_404
    creative = get_object_or_404(Creative, name__iexact=name)
    
    context = {
        'display_name': creative.display_name,
        'role': creative.role,
        'color': creative.color,
        'image_path': f"images/{creative.profile_image_filename}",
        'bio': creative.bio,
    }
    return render(request, 'member_blog.html', context)