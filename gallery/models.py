from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Flower(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='flower/')
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs):
        self.slug = slugify(self.title)
        super(Flower,self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('gallery:flower_details', kwargs={'slug':self.slug})