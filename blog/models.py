from django.db import models
from django.conf import settings
from mdeditor.fields import MDTextField
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.


class Category(models.Model):
    """文章分类"""
    title = models.CharField(max_length=100, unique=True)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_time']
        verbose_name = verbose_name_plural = "分类"

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    """文章"""
    title = models.CharField(max_length=100)
    summery = models.TextField(
        null=True,
        blank=True,
    )
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    tags = TaggableManager(verbose_name="标签", blank=True)
    content = MDTextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="articles")
    category = models.ForeignKey(Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name="articles")
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Blog: %s>" % (self.title)

    class Meta:
        ordering = ['-created_time']
        verbose_name = verbose_name_plural = "博客"
