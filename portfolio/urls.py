from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('blog',views.handleblog,name='handleblog'),
    path('internshipdetails',views.internshipdetails,name='internshipdetails'),
    path('skill',views.skill,name='skill'),
]
