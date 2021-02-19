from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView,LoginView,HomeView,home




urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('userhome/',HomeView.as_view(),name='userhome'),
    path('',home,name='home'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = 'updatebank/password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name = 'updatebank/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = 'updatebank/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'updatebank/password_reset_complete.html'),name='password_reset_complete'),

    ]   