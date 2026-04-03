from django.shortcuts import render, redirect
from .models import Contact


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

def member_blog(request, name):
    creatives = {
        'paul': {
            'display_name': 'PAUL',
            'role': 'VISUAL_ENGINEER',
            'color': '#ff4d4d',
            'profile_image': 'nganya3.png',
            'bio': """Paul is a visual engineer at Valgus whose work sits at the intersection of design and precision. With a strong eye for detail and a deep understanding of visual systems, he consistently delivers graphics that are not only aesthetically striking but also purposeful. His approach blends creativity with structure, allowing him to transform ideas into clean, engaging visuals that elevate the brand’s identity.

What sets Paul apart is his ability to think beyond surface-level design. He approaches each project with intention, ensuring that every element color, typography, layout works in harmony. His contributions play a key role in shaping the visual language of Valgus, making complex ideas feel intuitive and visually compelling.
""",
        },

'lovis': {
    'display_name': 'LOVIS',
    'role': 'ARCHITECTURAL_NODE // PERCUSSION',
    'color': '#ff4d4d', 
    'profile_image': 'lolo3.png', 
    'bio': """
        Lovis is a creative force with a sharp eye for capturing moments that feel natural. His photography stands out for its clarity, mood, and ability to tell a story without words. Whether behind the lens or behind the scenes, he brings a calm focus that translates into striking visuals.

Beyond photography, Lovis is a skilled drummer, channeling rhythm and energy into his band with precision and passion. This sense of timing and expression carries into his broader creative pursuits, including his path as an aspiring architect. With a growing interest in structure, space, and design, he is steadily shaping a future that blends artistry with form turning ideas into something both functional and beautiful.

    """
},
    }
    context = creatives.get(name.lower())
    
    if not context:
        from django.http import Http404
        raise Http404("Creative Not Found")

    # 4. Return the template
    return render(request, 'member_blog.html', context)