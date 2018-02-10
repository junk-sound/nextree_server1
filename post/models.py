from django.db import models
from django.contrib.auth.models import User
from tema.models import Tema
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    # hyper_link = hyper_link
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    title = models.CharField('TITLE', max_length=100)
    url = models.URLField('url')
    description = models.CharField('DESCRIPTION',max_length=200, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    # tag = tag
    # is_read = is_read

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)
