from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    img = models.ImageField(default= 'default.jpg' , upload_to='profile_pics')
    def __str__(self):
        return f'{self.user} Profile'

    def save(self):
        super().save()
        im = Image.open(self.img.path)

        if im.height > 300 or im.width > 300 :
            output_size = (300,300)
            im.thumbnail(output_size)
            im.save(self.img.path)