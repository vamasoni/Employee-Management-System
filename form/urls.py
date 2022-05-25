from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user_details', views.user_details, name='user_details'),
    path('details', views.details, name='details'),
    path('change_password', views.change_password, name='change_password' ),
    path('change_pwd', views.change_pwd, name='change_pwd'),
    path('update', views.update, name='update'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),

]

"""
path('', views.home, name='home'),
1. Submit Email form                        //PasswordResetView.as_view()
2. Email Sent success message               //PasswordResetDoneView.as_view()
3. Link to password reset form in email     //PasswordResetConfirmView.as_view()
4. Password successfully changed message    //PasswordResetCompleteView.as_view()
"""