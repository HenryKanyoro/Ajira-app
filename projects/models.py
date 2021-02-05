from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    photo = CloudinaryField('images')
    Bio = models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    datecreated= models.DateField(auto_now_add=True )

    def __str__(self):
        return self.user.username
 
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Projects(models.Model):
    Job_type = models.CharField(max_length=30)
    location = models.CharField(max_length=30,default='')
    salary = models.CharField(max_length=30,default='')
    contacts = models.CharField(max_length=30,default='')
    qualification = models.TextField(max_length=300)
    description = models.TextField(max_length=300)
    projectscreenshot = CloudinaryField('images')
    companyurl= models.URLField(max_length=200,blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    datecreated= models.DateField(auto_now_add=True )

    def save_projects(self):
        self.user

    def delete_projects(self):
        self.delete()    


    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(Job_type__icontains=name).all()

