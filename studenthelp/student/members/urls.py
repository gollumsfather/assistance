from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('members/', views.question_view, name='question'),
    path('math/', views.answer_view, name='math')
]