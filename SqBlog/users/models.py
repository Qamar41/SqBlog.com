from django.db import models
from django.contrib.auth.models import User
from PIL import Image

import PIL
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics' , blank=True)
    Address=models.CharField(max_length=64, default='Not Provided Yet' , blank=True)
    profession=models.CharField(max_length=30,default='' , blank=True)
    desccription=models.CharField(max_length=100,default='Hi There I am Single yet ...... ' , blank=True)
    # desccription=RichTextUploadingField(max_length=100)

    whattsapp=models.CharField(max_length=20, default='Not Provided Yet', blank=True)

    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)






