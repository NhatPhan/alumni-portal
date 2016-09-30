from django.conf.urls import url, include
from authentication import views
from django.views.generic import TemplateView, RedirectView
from .views import MySignupView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="authentication/login.html"), name='home'),
    url(r'^signup/$', TemplateView.as_view(template_name="authentication/signup.html"),
        name='signup'),
    url(r'^email-verification/$',
        TemplateView.as_view(template_name="authentication/email_verification.html"),
        name='email-verification'),
    url(r'^login/$', TemplateView.as_view(template_name="authentication/login.html"),
        name='login'),
    url(r'^logout/$', TemplateView.as_view(template_name="authentication/logout.html"),
        name='logout'),
    url(r'^password-reset/$',
        TemplateView.as_view(template_name="authentication/password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="authentication/password_reset_confirm.html"),
        name='password-reset-confirm'),

    url(r'^user-details/$',
        TemplateView.as_view(template_name="authentication/user_details.html"),
        name='user-details'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="authentication/password_change.html"),
        name='password-change'),


    # this url is used to generate email content
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="authentication/password_reset_confirm.html"),
        name='password_reset_confirm'),
]