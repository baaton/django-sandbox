from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    article_id = models.IntegerField()
    parent_id = models.IntegerField()
    date = models.DateTimeField()
    body = models.TextField()
    user_name = models.CharField(max_length=250)
    article_single = models.ForeignKey(Article)

    def __str__(self):
        return self.user_name
