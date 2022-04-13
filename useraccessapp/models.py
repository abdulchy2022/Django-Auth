from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=250,null=True)
   phone = models.CharField(max_length=250,null=True)
   email = models.CharField(max_length=250,null=True)
   address = models.CharField(max_length=200, null=True, blank=True)
   image = models.ImageField(default='default.jpg', upload_to='profile_pics')
   
   def __str__(self):
        return f'{self.user.username} Profile'