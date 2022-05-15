from django.db import models


# Create your db models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

# to display title in the django administration
    def __str__(self):
        return self.title