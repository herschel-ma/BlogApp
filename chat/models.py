from django.db import models


class Message(models.Model):
    room = models.CharField(max_length=100, verbose_name='房间名')
    message = models.TextField(verbose_name='消息')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    sender = models.CharField(max_length=100, verbose_name='发送者')

    def __str__(self):
        return self.message[:20]

    class Meta:
        db_table = "tb_chat"
        ordering = ("created_time", )
        verbose_name = "聊天记录表"
        verbose_name_plural = "聊天记录表"
