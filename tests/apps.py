from django.apps import AppConfig

from django_counter_cache_field import connect_counter


class TestsConfig(AppConfig):
    name = 'tests'

    def ready(self):
        super(TestsConfig, self).ready()

        from tests.models import Article
        connect_counter('published_count', Article.user, lambda article: not article.is_draft)
        connect_counter('draft_count', Article.user, lambda article: article.is_draft)

        from tests.models import Relationship
        connect_counter('following_count', Relationship.consumer)
        connect_counter('followers_count', Relationship.producer)
