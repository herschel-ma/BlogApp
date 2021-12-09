from django.db.models.signals import pre_save
from .models import Blog
from django.dispatch import receiver
from slugify import slugify
# from django.utils.text import slugify
from lxml import etree
import markdown


@receiver(pre_save, sender=Blog)
def article_add_slug(sender, instance, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title, only_ascii=True)
        instance.slug = slug


@receiver(pre_save, sender=Blog)
def create_auth_token(sender, instance=None, **kwargs):
    if instance and not instance.summery:
        html = markdown.markdown(instance.content)
        summery = etree.HTML(html)
        instance.summery = summery.xpath("string()")[:120]
