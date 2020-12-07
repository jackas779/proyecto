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
        super().save()

        image = Image.open(self.image.path)
        #To resize the profile image
        if image.height > 400 or image.width > 400:
            output_size = (400, 400)
            image.thumbnail(output_size)
            image.save(self.image.path)
