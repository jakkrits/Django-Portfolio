from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/blog')

    def __str__(self):
        return f'{self.title.title()}: published: {self.pub_date}'
