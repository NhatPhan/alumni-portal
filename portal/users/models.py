from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    # Link UserProfile to User model instance
    user = models.OneToOneField(User)
    
    
    # Additional attributes
    dateofbirth = models.DateField()
    personal_email = models.EmailField()
    field_of_work = models.CharField(max_length=128)
    linkedin = models.URLField()
    facebook = models.URLField()
    biography = models.TextField()
    hobby = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile_images')
    team_members = models.ManyToManyField('UserProfile')
    is_completed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.user.username


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
    

        
