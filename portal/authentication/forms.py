from django import forms
from users.models import UserProfile


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    class Meta:
        model = UserProfile

    def signup(self, request, user):
        profile = UserProfile()
        profile.save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        user.profile = profile
        profile.user = user     
        profile.save()
        user.save()