from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
]