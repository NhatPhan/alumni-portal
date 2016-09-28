from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ProfileView, UserList, index, ProfileView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profile/(?P<pk>[0-9]+)/$', login_required(ProfileView.as_view()), name='profile'),
    url(r'^profile/(?P<pk>[0-9]+)/(?P<team_member_pk>[0-9]+)$', login_required(ProfileView.as_view()), name='add_team_member'),
    url(r'^users/$', login_required(UserList.as_view()), name='users'),
    url(r'^users/(?P<search>[\w]+)/$', login_required(UserList.as_view()), name='users'),
]