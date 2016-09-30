from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from .models import UserProfile, Project, Education, Job, Location
from django.forms.widgets import SelectDateWidget   
        

class UserProfileForm(forms.ModelForm):
    personal_email = forms.EmailField(required=False)
    biography = forms.CharField(widget=forms.Textarea, required=False)
    hobby = forms.CharField(max_length=256, required=False)
    dateofbirth = forms.DateField(widget=SelectDateWidget(years=range(1970, 2016)), required=False)
    field_of_work = forms.CharField(max_length=128, required=False)
    linkedin = forms.URLField(required=False)
    facebook = forms.URLField(required=False)
    address = forms.CharField(max_length=256, required=False)
    gender = forms.CharField(max_length=10, required=False)
    is_completed = forms.BooleanField(required=False)
    
    class Meta:
        model = UserProfile
        fields = ('dateofbirth', 'personal_email', 'field_of_work', 'linkedin', 'facebook', 'biography', 'hobby', 'is_completed', 'address', 'gender')
        

ProjectFormSet = inlineformset_factory(UserProfile, Project, fields=('user', 'name', 'from_date', 'to_date', 'description'), widgets={
    'from_date': SelectDateWidget(years=range(2000, 2030)), 'to_date': SelectDateWidget(years=range(2000, 2030))
})

EducationFormSet = inlineformset_factory(UserProfile, Education, fields=('user', 'school', 'class_of', 'major', 'achievements', 'activities'))

JobFormSet = inlineformset_factory(UserProfile, Job, fields=('user', 'title', 'from_date', 'to_date', 'location', 'description'), widgets={
    'from_date': SelectDateWidget(years=range(2000, 2030)), 'to_date': SelectDateWidget(years=range(2000, 2030))
})

LocationFormSet = inlineformset_factory(UserProfile, Location, fields=('user', 'name', 'address', 'city', 'zipcode', 'position'),max_num = 1, extra = 1, can_delete=False)