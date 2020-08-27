from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='bresume/images/')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={
             'project_id':self.id
        })