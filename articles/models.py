from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.title