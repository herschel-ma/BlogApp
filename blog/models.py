from django.db import models
from django.conf import settings
from mdeditor.fields import MDTextField
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.


class ArticleManager(models.Manager):
    def distinct_date(self):  # 该管理器定义了一个distinct_date方法，目的是找出所有的不同日期
        distinct_date_list = []  # 建立一个列表用来存放不同的日期 年-月
        date_list = self.values(
            'created_time')  # 根据文章字段date_publish找出所有文章的发布时间
        for date in date_list:  # 对所有日期进行遍历，当然这里会有许多日期是重复的，目的就是找出多少种日期
            date = date['created_time'].strftime(
                '%Y-%m')  # 取出一个日期改格式为 ‘xxx年/xxx月 存档’
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


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
    objects = ArticleManager()  # 在模型中使用自定义的管理器

    def __str__(self):
        return "<Blog: %s>" % (self.title)

    class Meta:
        ordering = ['-created_time']
        verbose_name = verbose_name_plural = "博客"
