# app/management/commands/generate_fake_data.py

import random
from django.core.management.base import BaseCommand
from faker import Faker
from website1.models import Task

class Command(BaseCommand):
    help = 'Generate fake user profiles'

    def handle(self, *args, **kwargs):
        fake = Faker()
        number_of_profiles = 10
        for _ in range(number_of_profiles):
            Task.objects.create(
                name=fake.sentence(nb_words=10),
                content=fake.text()
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully created {number_of_profiles} Post.'))