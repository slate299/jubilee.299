from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('leadership/', views.leadership, name='leadership'),
    path('achievements/', views.achievements, name='achievements'),
    path('events/', views.events, name='events'),
    path('join/', views.join_movement, name='join_movement'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('search/', views.search, name='search'),  # for search results
]
