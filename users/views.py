import secrets

from django.contrib.auth import logout
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import CustomUser


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('catalog:product_list'))


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        print("asdsadsa")
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)

        user.token = token
        user.save()

        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}"
        print(url)
        send_mail(
            subject="Тема письма",
            message=f"Перейдите по ссылке {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("catalog:product_list"))
