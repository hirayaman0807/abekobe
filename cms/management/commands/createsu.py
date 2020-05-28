from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="abekobechat").exists():
            User.objects.create_superuser(username="abekobechat", email="hirayaman0807@gmail.com", password="dudzYh-3feksu-qafdoq")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))