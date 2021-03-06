from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.urls import reverse

from industry.models import IndustryName


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField(max_length=70,unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    factoryName = models.ForeignKey(IndustryName, null=True,on_delete=models.CASCADE, related_name='FactoryName')

    def __str__(self):
        return f'{self.user.username}  and  {self.factoryName}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class contact(models.Model):
    factoryname = models.CharField(max_length=50)
    email = models.EmailField()
    Message = models.TextField()
    def __str__(self):
        return self.factoryname
class CommentBox(models.Model):
    name = models.TextField()