

from django.urls import path
from .views import search_images, save_favorite, view_favorites, delete_favorite, delete_by_url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index_page, name='index'),
    path('home/', search_images, name='home'),
    path('save_favorite/', save_favorite, name='save_favorite'),
    path('favorites/', view_favorites, name='view_favorites'),
    path('delete_favorite/<int:pk>/', delete_favorite, name='delete_favorite'),
    path('delete_by_url/', delete_by_url, name='delete_by_url'),
    path('login/', auth_views.LoginView.as_view(template_name='gallery/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/home/'), name='logout'),
    path('register/', views.register, name='register'),
    


]


