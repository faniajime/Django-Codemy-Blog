from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
       return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length = 255, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
        
    def get_absolute_url(self):
       return reverse('home')
   
    def total_comments(self):
        return self.comments.count()
   
class Comment(models.Model):   
    post = models.ForeignKey(Post,related_name="comments", on_delete = models.CASCADE)
    email = models.CharField(max_length=255)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s ' % (self.post.title, self.name)
