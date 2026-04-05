from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Creative(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    display_name = models.CharField(max_length=100)     
    role = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#ff4d4d')
    profile_image_filename = models.CharField(max_length=100) 
    bio = models.TextField()

    def __str__(self):
        return self.display_name
    
class Vblog(models.Model):
    heading= models.CharField(max_length=30, unique=True)
    description= models.TextField()
    preview_image= models.ImageField (upload_to='blog_images/')
    date= models.DateField(auto_now=True)

    def __str__(self):
        return self.heading

class blog(models.Model):
    date = models.DateField(auto_now=True)
    main_title = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=40)
    blog_image = models.ImageField (upload_to='blog_images/')
    lead_text = models.TextField(null=True)
    sub_heading = models.CharField(max_length=30)
    block_quote = models.TextField(null=True)
    full_blog = models.TextField(null=True)

    def __str__(self):
        return self.main_title