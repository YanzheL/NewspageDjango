from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class News(models.Model):

    title = models.CharField(max_length=10000)
    url = models.CharField(max_length=1000)

    # def __unicode__(self):
    #     return self.title
