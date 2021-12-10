from django.db import models
from users.models import userModel
from mdeditor.fields import MDTextField
from blog.models import Blog


class Comment(models.Model):
    """评论模型"""
    author = models.ForeignKey(userModel,
                               on_delete=models.CASCADE,
                               related_name='comments')
    article = models.ForeignKey(Blog,
                                on_delete=models.CASCADE,
                                related_name='comments')
    content = MDTextField()
    created_time = models.DateTimeField(auto_now_add=True)
    isShow = models.BooleanField(default=True)
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL,
                               related_name='children')

    class Meta:
        ordering = ['-created_time']
        verbose_name = verbose_name_plural = "评论"

    def __str__(self):
        return self.content[:20]
