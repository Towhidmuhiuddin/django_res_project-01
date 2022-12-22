from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.deshboard, name='Deshboard'),
    path('home/', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('blog/', views.blog, name='Blog'),
    path('contract', views.contract, name='Contract'),
]