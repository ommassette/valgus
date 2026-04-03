from django.db import models

# Create your models here.
# shop/models.py

class Website(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    preview_link = models.URLField()
    image = models.ImageField(upload_to='websites/')

    def __str__(self):
        return self.name