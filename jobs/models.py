from django.db import models


class Job(models.Model):
    # images go to /media/images/...
    image = models.ImageField(upload_to='images/job')
    description = models.TextField(max_length=200)
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'Job: {self.title.upper()}'

