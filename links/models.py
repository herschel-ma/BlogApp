from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    "友链分类"
    title = models.CharField(max_length=50, unique=True, help_text="类别")
    created_time = models.DateTimeField(default=timezone.now, help_text="添加时间")

    class Meta:
        ordering = ['-created_time']
        verbose_name = verbose_name_plural = "分类"

    def __str__(self) -> str:
        return self.title


class LinksThumbnail(models.Model):
    content = models.ImageField(upload_to="links/%Y/%m/%d/")


class Links(models.Model):
    """友链"""
    SHOWCHOICES = ((False, "不展示"), (True, "展示"))
    title = models.CharField(max_length=50, unique=True, help_text="标题")
    description = models.TextField(null=True, blank=True, help_text="描述")
    show = models.BooleanField(choices=SHOWCHOICES,
                               default=False,
                               help_text="是否展示")
    thumbnail_url = models.URLField(blank=True, null=True, help_text="封面")
    link_url = models.URLField(blank=True, null=True, help_text="链接地址")

    category = models.ForeignKey(Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='links',
                                 help_text="友链分类")

    created_time = models.DateTimeField(default=timezone.now, help_text="创建时间")
    last_updated_time = models.DateTimeField(auto_now=True, help_text="更新时间")

    def __str__(self):
        return "友链: %s" % (self.title)

    class Meta:
        ordering = ["-created_time"]
        verbose_name = verbose_name_plural = "友链"
