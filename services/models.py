from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Service(models.Model):
    title = models.CharField(max_length=100)
    fafa = models.CharField(max_length=100, blank=False, null=True)  
    statements = RichTextField(max_length=400, blank=True, null=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title