from django.contrib import admin
from .models import Post,Comment,Announcement
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Announcement)