from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from  django.urls import reverse
from ckeditor_uploader.fields import  RichTextUploadingField
from datetime import datetime


# Create your models here.
#
# class Category(models.Model):
#     name=models.CharField(max_length=255)
#
#
#     def __str__(self):
#         return self.name
#
#
#     # def get_absolute_url(self):
#     #     return reverse('post-detail',kwargs={'pk':self.pk})
    #




class Post(models.Model):
    title=models.CharField(max_length=100)
    # content=models.TextField()
    post_overview=RichTextUploadingField()
    content = RichTextUploadingField()
    date_posted=models.DateTimeField(datetime.now, default=datetime.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    # list_date = models.DateTimeField(datetime.now, default=datetime.now)
   
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email =	models.EmailField()
    body =	models.TextField()
    created	= models.DateTimeField(auto_now_add=True)
    updated	= models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
	
    class Meta:
        ordering = ('created',)
	
    
    def	__str__(self):
        return	'Comment	by	{}	on	{}'.format(self.name,	self.post)






class Announcement(models.Model):
    title=models.CharField(max_length=100)
    # content=models.TextField()
    annoncement_overview=RichTextUploadingField()
    Announcement_details = RichTextUploadingField()
    date_posted=models.DateTimeField(datetime.now, default=datetime.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return 'Announcement	by	{}	on	{}'.format(self.title,self.author ,self.date_posted)
