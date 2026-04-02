from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')
def services(request):
    return render(request,'services.html')
def vblog(request):
    return render(request,'vblog.html')
def blogs(request):
    return render(request,'blogs.html')
# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         query = Contact(name=name, email=email, subject=subject, message=message) 
#         query.save()

#         return redirect('my_index')
#     return render (request, 'index.html')

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