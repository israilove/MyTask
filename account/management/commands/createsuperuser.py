from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Create a superuser.'

    def handle(self, *args, **options):
        email = options.get('email')
        username = options.get('username')

        if email and not username:
            options['username'] = email

        try:
            return super().handle(*args, **options)
        except ValidationError as e:
            self.stderr.write('\n'.join(e.messages))
            self.stderr.write('')
