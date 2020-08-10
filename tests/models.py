from django.db import models

from django_counter_cache_field import CounterCacheField


class User(models.Model):
    name = models.CharField(max_length=100)
    following_count = CounterCacheField()
    followers_count = CounterCacheField()
    published_count = CounterCacheField()
    draft_count = CounterCacheField()


class Relationship(models.Model):
    consumer = models.ForeignKey('User', related_name='producer_set', on_delete=models.CASCADE)
    producer = models.ForeignKey('User', related_name='consumer_set', on_delete=models.CASCADE)


class Article(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True)
