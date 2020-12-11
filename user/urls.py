#Django
from django.urls import path
from django.contrib.auth import views
#Views
from .views import profile, password_change

urlpatterns = [
    #Perfil
    path('profile/', profile, name="profile"),
    path('password_change/', password_change, name="change"),
    path('password_reset/', views.PasswordResetView.as_view(template_name='user/passwordResetForm.html', html_email_template_name='user/send_email.html', subject_template_name = 'user/password_reset_subject.txt'), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='user/passwordResetDone.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='user/passwordSetForm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetCompleteView.as_view(template_name='user/passwordResetComplete.html'), name='password_reset_complete'),
]