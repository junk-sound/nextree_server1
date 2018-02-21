from django.db import models
from account.models import User
from topic.models import Topic
from tema.models import Tema
from django.utils.text import slugify
# Create your models here.


class Bookmark(models.Model):
    # hyper_link = hyper_link
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmark_user')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmark_writer')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    title = models.CharField('TITLE', max_length=80)
    url = models.URLField('url')
    description = models.CharField('DESCRIPTION',max_length=200, help_text='simple description text')
    create_date = models.DateTimeField(auto_now_add=True)
    post_modify_date = models.DateField(auto_now=False, auto_now_add=False)
    post_published_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, default=None)
    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username+'-'+self.title, allow_unicode=True)
        super(Bookmark, self).save(*args, **kwargs)