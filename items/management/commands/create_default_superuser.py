from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a default root superuser if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = 'root'
        password = 'uo]n/Zfs+omwY{fy0$Q+{>}Cl+ryF4'
        email = 'root@example.com'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser "{username}"'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists'))