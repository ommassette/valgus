from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Added for tracking

    def __str__(self):
        return self.name
    
class Creative(models.Model):
    name = models.CharField(max_length=50, unique=True) # Used in URL (e.g., 'paul')
    display_name = models.CharField(max_length=100)      # Used in UI (e.g., 'PAUL')
    role = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#ff4d4d')
    profile_image_filename = models.CharField(max_length=100) # Filename in static/images/
    bio = models.TextField()

    def __str__(self):
        return self.display_name