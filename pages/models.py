from django.db import models

# Create your models here.



class Students(models.Model):
    
    Gender = (
        ('M', 'male'),
        ('F', 'female'),
    )
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    Photo = models.ImageField(upload_to='photos/', blank=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(choices=Gender, max_length=6)
    is_admitted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name 
