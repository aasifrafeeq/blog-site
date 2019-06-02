from django.db import models

class Blog(models.Model):
    heading = models.CharField(max_length=24)
    content = models.CharField(max_length = 999999999999,default='content')

    def __str__(self):
        return self.heading+'  '+self.content

# Create your models here.
