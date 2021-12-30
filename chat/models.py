from django.db import models
from users.models import userModel


class Message(models.Model):
    sender = models.ForeignKey(userModel,
                               on_delete=models.CASCADE,
                               related_name='sender',
                               verbose_name='发送者'),
    message = models.TextField(verbose_name='消息')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.message[:20]

    class Meta:
        db_table = "tb_chat"
        ordering = ("created_time", )
        verbose_name = "聊天记录表"
        verbose_name_plural = "聊天记录表"
