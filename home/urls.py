from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('hero/', views.hero, name='hero'),
    path('hero/update/<int:id>', views.hero_update, name="hero")
]
