from django.db import models

class Website(models.Model):
    # Core Identity (Text-Based Utility)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Navigation Link
    preview_link = models.URLField(max_length=500)
    
    # Metadata for Backend Logic
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        # Keeps the newest ready-made systems at the top
        ordering = ['-created_at']

    def __str__(self):
        return f"SYSTEM_NODE: {self.name}"