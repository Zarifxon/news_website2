from django.urls import path
from .views import dashboard_view,  logout_view
from .views import user_login,user_register, edit_user, EditUserView
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView
)

urlpatterns = [
    # path('login/', user_login, name='login'),

    path('login/', LoginView.as_view(), name='login'),

    path('logout/', logout_view, name="logout"),



    # Parolni o'zgartish
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Parolni qayta tiklash
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),\

    path('profile/', dashboard_view, name="user_profile"),
    path("signup/", user_register, name="user_register"),
    path("profile/edit/", edit_user, name="edit_user_information"),
    # path("profile/edit/", EditUserView.as_view(), name="edit_user_information"),
    # path("signup/", SignUpView.as_view(), name="user_register")








]