from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@exsample.com',
            first_name='Admin',
            last_name='Adminex'
        )
        user.set_password('123qwe')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Успешно создан пользователь-администратор с электронной почтой {user.email}'))
