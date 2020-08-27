from django.db import models
from django.urls import reverse
from tinymce import HTMLField
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='blog/images/', blank=True)
    comment_count = models.IntegerField(default=0)
    content = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={
            'blog_id':self.id
        })
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    blog = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

