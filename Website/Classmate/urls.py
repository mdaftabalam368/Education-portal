from django.urls import path
from . import views

app_name = 'Classmate'

urlpatterns = [
    path('<int:course_id>/', views.Details, name='Details'),
    path('', views.Courses, name='home_page'),
    path('logout/', views.logout_request, name='logout'),
    path('Login/', views.login_request, name='login'),
    path('Register/', views.register, name='register'),
    path('<int:course_id>/yourchoice/', views.yourchoice, name='yourchoice'),
    path('description', views.description, name='description'),
    path('About', views.about, name='about'),
    path('Blog', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('Home_page', views.home, name='Home'),
    path('Search',views.search, name='search_page')
]
