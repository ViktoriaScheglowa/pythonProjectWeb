from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UsersConfig
from users.views import CustomLogoutView, UserCreateView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name='login'),
    path("logout/", CustomLogoutView.as_view(), name='logout'),
    path("registration/", UserCreateView.as_view(), name='registration'),
    path("email-confirm/<str:token>", email_verification, name='email_confirm'),
]