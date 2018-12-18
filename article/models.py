from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100) # blog's title
    category = models.CharField(max_length=50) # blog's lag
    date_time = models.DateTimeField(auto_now_add=True) # blog's date
    content = models.TextField(blank=True, null=True) # blog's content

    def __unicode__(self):
        return self.title

    class Meta: # order by time desc
        ordering = ['-date_time']

