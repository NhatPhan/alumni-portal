from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView, DetailView
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from itertools import chain

from .models import UserProfile, Project, Education, Job
from .serializers import UserSerializer, UserProfileSerializer, ProjectSerializer, EducationSerializer, JobSerializer
from .forms import UserProfileForm, ProjectFormSet, EducationFormSet, JobFormSet

@login_required
def index(request):
    return redirect('profile/' + str(request.user.id))


class ProfileView(ModelFormMixin, DetailView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "users/profile.html"
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        project_form = ProjectFormSet(instance=self.object)
        education_form = EducationFormSet(instance=self.object)
        job_form = JobFormSet(instance=self.object)
        return self.render_to_response(
            self.get_context_data(form=form,
                                  project_form=project_form, education_form=education_form, job_form=job_form))
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

    def get_context_data(self, form, project_form, education_form, job_form, **kwargs):
        user_profile = UserProfile.objects.get(user__id=self.kwargs.get('pk'))
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['form'] = form
        context['project_form'] = project_form
        context['education_form'] = education_form
        context['job_form'] = job_form
        return context
        
    def get_object(self,**kwargs):
        user_profile = UserProfile.objects.get(user__id=self.kwargs.get('pk'))
        team_member_pk = self.kwargs.get('team_member_pk')
        if team_member_pk:
            team_member = UserProfile.objects.get(user__id=team_member_pk)
            if team_member and team_member not in user_profile.team_members.all() :
                user_profile.team_members.add(team_member)
                return team_member
        return user_profile
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        project_form = ProjectFormSet(self.request.POST, instance=self.object)
        education_form = EducationFormSet(self.request.POST, instance=self.object)
        job_form = JobFormSet(self.request.POST, instance=self.object)
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        if form.is_valid() and project_form.is_valid() and education_form.is_valid() and job_form.is_valid():
            return self.form_valid(form, project_form, education_form, job_form)
        else:
            return self.form_invalid(form, project_form, education_form, job_form)
    
    def form_valid(self, form, project_form, education_form, job_form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        self.object = form.save()
        project_form.instance = self.object
        project_form.save()
        education_form.instance = self.object
        education_form.save()
        job_form.instance = self.object
        job_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, project_form, education_form, job_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  project_form=project_form, education_form=education_form, job_form=job_form))
        

class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/users.html'

    def get(self, request):
        search_term = request.GET.get('search')
        if search_term:
            userprofiles_queryset = UserProfile.objects.filter(Q(user__first_name__contains=search_term) | Q(user__last_name__contains=search_term) | Q(user__email__contains=search_term))
        else:
            userprofiles_queryset = UserProfile.objects.all()
        return Response({'userprofiles': userprofiles_queryset})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer