from django.db import models

# Create your models 

class  Testimonials(models.Model):
    individualname = models.CharField(max_length=200)
    title          =  models.CharField(max_length=200)
    body           = models.TextField()
    image          = models.ImageField(upload_to="pics")

