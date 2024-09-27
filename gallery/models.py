from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# from django.utils.translation import gettext as _
# Create your models here.

# class Flower(TranslatableModel):
#     # الحقول التي لا تحتاج إلى ترجمة
#     slug = models.SlugField(blank=True, null=True)
#     image = models.ImageField(upload_to='flower/')

#     # الحقول القابلة للترجمة
#     translations = TranslatedFields(
#         title=models.CharField(max_length=100),
#         description=models.TextField(),
#     )
class Flower(models.Model):
    title = models.CharField(max_length=100)#,verbose_name=_('title')
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='flower/')#,verbose_name=_('image')
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs):
        self.slug = slugify(self.title)
        super(Flower,self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('gallery:flower_details', kwargs={'slug':self.slug})