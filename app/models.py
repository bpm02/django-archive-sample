from django.db import models
from django.utils import timezone


class PostQuerySet(models.QuerySet):

    def published(self):
        return self.filter(created_at__lte=timezone.now())


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title
