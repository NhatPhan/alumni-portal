from rest_framework import serializers

from .models import UserProfile, Project, Education, Job
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('dateofbirth', 'personal_email', 'field_of_work', 'linkedin', 'facebook', 'biography', 'hobby', 'is_completed', 'team_members')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'year', 'description')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('school', 'class_of', 'major', 'achievements', 'activities')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title', 'from_date', 'to_date', 'location', 'description')