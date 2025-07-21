from django.db import models

# Create your models here.
class Country(models.Model):
    title = models.CharField(max_length=30)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class City(models.Model):
    title = models.CharField(30)
    image = models.ImageField(upload_to='city_rasm/', null=True, blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    counrty = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
