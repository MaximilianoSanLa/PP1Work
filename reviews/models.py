from django.db import models

# Create your models here.
class reviews(models.Model):
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image= models.ImageField(upload_to='reviews/images/')
    url= models.URLField(blank=True)
    genre= models.CharField(blank=True, null=True, max_length=100)
    year= models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.title