from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@user.com',
            first_name='Admin1',
            last_name='Adminexin'
        )
        user.set_password('1234qwer')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Успешно создан пользователь-администратор с электронной почтой {user.email}'))
