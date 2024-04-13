from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    main_title = models.CharField(max_length=200, null=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True)
    sub_title1 = models.CharField(max_length=200, null=True)
    img1 = models.ImageField(null=True, blank=True)
    paragraph1 = models.CharField(max_length=2000, null=True)
    sub_title2 = models.CharField(max_length=200, null=True)
    img2 = models.ImageField(null=True, blank=True)
    paragraph2 = models.CharField(max_length=2000, null=True)
    sub_title3 = models.CharField(max_length=200, null=True)
    img3 = models.ImageField(null=True, blank=True)
    paragraph3 = models.CharField(max_length=2000, null=True)
    sub_title4 = models.CharField(max_length=200, null=True)
    img4 = models.ImageField(null=True, blank=True)
    paragraph4 = models.CharField(max_length=2000, null=True)
    
