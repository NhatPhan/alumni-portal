"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView, RedirectView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from users import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'educations', views.EducationViewSet)
router.register(r'jobs', views.JobViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include('users.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
    url(r'^authentication/', include('authentication.urls')),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/logout/', RedirectView.as_view(url='/'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
