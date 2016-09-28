from django.shortcuts import render
from django.http import request, HttpResponse
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.account.views import SignupView, LoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class MySignupView(SignupView):
    template_name = 'authentication/signup.html'


class MyLoginView(LoginView):
    template_name = 'authentication/login.html'