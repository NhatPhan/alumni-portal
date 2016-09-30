from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.db import models
from geoposition.fields import GeopositionField

    
class UserProfile(models.Model):
    # Link UserProfile to User model instance
    user = models.OneToOneField(User)
    
    
    # Additional attributes
    dateofbirth = models.DateField(null=True)
    personal_email = models.EmailField(blank=True)
    field_of_work = models.CharField(max_length=128)
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    biography = models.TextField(blank=True)
    hobby = models.CharField(blank=True, max_length=256)
    gender = models.CharField(blank=True, max_length=10)
    image = models.ImageField(upload_to='profile_images')
    team_members = models.ManyToManyField('UserProfile')
    is_completed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.user.username


class Location(models.Model):
    # Link UserProfile to User model instance
    user = models.ForeignKey(UserProfile, blank=True)
    
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    position = GeopositionField(blank=True)

    class Meta:
        verbose_name_plural = 'locations'
        

class Project(models.Model):
    user = models.ForeignKey(UserProfile, blank=True)
    name = models.CharField(max_length=128, blank=True)
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
    description = models.CharField(max_length=256, blank=True)
    
    def __unicode__(self):
        return self.name


class Education(models.Model):
    user = models.ForeignKey(UserProfile, blank=True)
    school = models.CharField(max_length=128, blank=True)
    class_of = models.IntegerField(blank=True)
    major = models.CharField(max_length=128, blank=True)
    achievements = models.TextField(blank=True)
    activities = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.school
    

class Job(models.Model):
    user = models.ForeignKey(UserProfile, blank=True)
    title = models.CharField(max_length=128, blank=True)
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
    location = models.CharField(max_length=128, blank=True)
    description = models.CharField(max_length=256, blank=True)
    
    def __unicode__(self):
        return self.title

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
    


        
