from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False,)
 
    def __str__(self):
        """String for representing the Model object."""
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    pic_url =  models.CharField(max_length=200, unique=True, null=True, blank=True)
    post_pic   = models.ImageField(upload_to='blog/', blank=True, null=True)
    content = RichTextField(null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ManyToManyField(Category,  help_text='Select a category for this Post')
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})