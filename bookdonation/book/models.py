from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # book_images = models.FileField(upload_to='book_images/%Y/%m/%d/', blank=True , null=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.user
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Book(models.Model):
    booktitle   = models.CharField(max_length=200, blank=False)
    authorname  = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    languages   = models.CharField(max_length=200, blank=False)
    #book_images = models.FileField(upload_to='book_images/%Y/%m/%d/', blank=True , null=True)
    image = models.ImageField(upload_to = 'pic_folder/', blank=False)
    def __str__(self):
        """String for representing the Model object."""
        return self.booktitle
    #bookphoto   = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
	

class Userinfo(models.Model):
    Name   = models.CharField(max_length=200, blank=False)
    Address  = models.CharField(max_length=200, blank=False)
    MobileNumber = models.IntegerField(default=0)
    PinCode   = models.IntegerField(default=0)
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.Name