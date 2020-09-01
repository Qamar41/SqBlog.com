from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from django.urls import reverse_lazy
from django.contrib.auth import views as aut_views
urlpatterns = [
    path('register',views.register , name='user-register'),
    path('',aut_views.LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/',aut_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/',views.profile , name='profile'),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),

    # Password Reset

    path('password-reset/', aut_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', aut_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', aut_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', aut_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]
