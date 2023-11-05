from django.conf import settings
from django.db import models
from django.utils import timezone


class Problem_posts(models.Model):
    fullname = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=30,null=False,blank=False)
    phonenumber=models.CharField(max_length=50,null=True,blank=True)
    problem = models.TextField(max_length=300,null=False,blank=False)
    date_created = models.DateTimeField()
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return f'{self.problem} by {self.fullname}'
    
    
 

# Create your models here.
