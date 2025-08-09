from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create default superuser if not exists and set password'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, default='asheesh')
        parser.add_argument('--email', type=str, default='appatel9839@gmail.com')
        parser.add_argument('--password', type=str, default='Apatel9839@')

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username']
        email = options['email']
        password = options['password']

        user, created = User.objects.get_or_create(username=username, defaults={'email': email, 'is_superuser': True, 'is_staff': True})
        if created:
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created superuser {username}'))
        else:
            # ensure staff/superuser flags and password are set/updated
            changed = False
            if not user.is_staff:
                user.is_staff = True; changed = True
            if not user.is_superuser:
                user.is_superuser = True; changed = True
            # update password if different
            user.set_password(password); changed = True
            if changed:
                user.save()
            self.stdout.write(self.style.SUCCESS(f'Updated superuser {username}'))
