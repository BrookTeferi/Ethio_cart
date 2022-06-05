from django.db import models

# Create your models here.
class catagory(models.Model):
    catagory_name = models.CharField(max_length=50,unique=True)
    slug=models.CharField(max_length=100,unique=True)
    description=models.TextField(max_length=255, blank=True)
    car_Img=models.ImageField(upload_to='photo/catagories',blank=True)
    class Meta:
        verbose_name = "catagory"
        verbose_name_plural = "Catagories"
    def __str__(self):
        return self.catagory_name   