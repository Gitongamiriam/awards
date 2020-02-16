from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    prof_pic = models.ImageField(upload_to='images/')
    bio = models.TextField(blank=True)
    objects = models.Manager()

    class Meta:
        ordering = ['bio']

    def save_profile(self):
        self.save()

    def get_user_projects(self):
        return self.project.all

    def __str__(self):
       return f'{self.user.username} Profile'


class Project(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="projects")
    title = models.CharField(max_length=150)
    description = HTMLField()
    project_pic = models.ImageField(null=True,upload_to="project/")
    pub_date = models.DateTimeField(auto_now_add=True)
    live_site =models.URLField(max_length=300,blank=True)
    objects = models.Manager()

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title_icontains=search_term)
        return project

