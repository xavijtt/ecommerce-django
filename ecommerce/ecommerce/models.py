from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='phtos/categories', blank=True)
    
    class Meta:
        verbose_name ='category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.category_name