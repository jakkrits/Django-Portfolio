import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')

import django
django.setup()

from faker import Faker
from jobs.models import Job

seed_fake = Faker()


def create_jobs():
    fake_image = seed_fake.url()
    fake_description = seed_fake.sentences(nb=10)
    fake_summary = seed_fake.sentences(nb=10)
    fake_title = seed_fake.company()

    job = Job.objects.get_or_create(
        image=fake_image,
        description=fake_description,
        summary=fake_summary,
        title=fake_title
    )
    job.save()

