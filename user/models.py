#Django
from django.db import models
from django.contrib.auth.models import User
#Pillow
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{} profile'.format(self.user.username)
    
    def save(self, *args, **kwargs):
        image = Image.open(self.image.path)
        image.save(self.image.path)
        super().save(*args, **kwargs)
