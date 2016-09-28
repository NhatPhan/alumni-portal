from django.contrib import admin

from users.models import UserProfile, Project, Education, Job

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Job)