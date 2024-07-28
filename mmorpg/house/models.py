from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    CAT = (('tank', 'танк'),
           ('healing', 'Хилы'),
           ('dd', 'ДД'),
           ('buy', 'Торговцы'),
           ('gild', 'Гилдмастеры'),
           ('quest', 'Квестгиверы'),
           ('smith', 'Кузнецы'),
           ('tanner', 'Кожевники'),
           ('potion', 'Зельевары'),
           ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title_name = models.CharField(max_length=128)
    text_post = models.TextField()
    category = models.CharField(max_length=18, choices=CAT, default='tank')


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.OneToOneField(User, on_delete=models.CASCADE)
    textPost = models.TextField()
    status = models.BooleanField(default=False)




