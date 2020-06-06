from django.urls import path
from .import views
from django.contrib.auth import views as aut_views
urlpatterns = [
    path('',views.register , name='user-register'),
    path('login/',aut_views.LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/',aut_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/',views.profile , name='profile'),
]
