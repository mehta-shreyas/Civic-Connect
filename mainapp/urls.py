from django.urls import include, path
from . import views
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

app_name = 'mainapp'
urlpatterns = [
    path('', TemplateView.as_view(template_name="mainapp/index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('createTemp/', views.makeTemplate, name='createTemp'),
    path('profile/', views.profile, name='profile'),
    path('editProfile/', views.edit_profile, name='editProfile'),
    path('browse/', views.browseTemplates, name='browse'),
    path("<int:id>", views.templatePage, name="templatePage"),
    path('news/', views.news, name='news'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("logout", views.logout_view, name="logout"),
    path('contact/', views.sendEmail, name='contact'),
    path('success/', views.successView, name='success'),
    path('sendEmail/',views.sendEmail, name='sendEmail'),
]
