from django.db import models
from django.conf import settings
from mdeditor.fields import MDTextField
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    content = MDTextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles")
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Blog: %s>" % (self.title)

    # def get_url(self):
    #     return reverse('blog:blog_detail', kwargs={'blog_pk': self.pk})

    class Meta:
        ordering = ['-created_time']
        verbose_name = verbose_name_plural = "博客"
