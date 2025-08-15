from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('leadership/', views.leadership, name='leadership'),
    path('achievements/', views.achievements, name='achievements'),
    path('legacy/', views.legacy, name='legacy'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('events/', views.events, name='events'),
    path('join/', views.join_movement, name='join_movement'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('big4/', views.big4, name='big4'),
    path('manufacturing/', views.manufacturing_view, name='manufacturing'),
    path('housing/', views.housing_view, name='housing'),
    path('healthcare/', views.healthcare_view, name='healthcare'),
    path('food-security/', views.food_security_view, name='food_security'),
    path('concerns/', views.concerns, name='concerns'),
    path('news/', views.news, name='news'),
    path('search/', views.search, name='search'),  # for search results
]
