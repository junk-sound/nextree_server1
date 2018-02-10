from django.db import models
from django.utils.text import slugify
# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField('Topic', max_length=100)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.topic_name, allow_unicode=True)
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.topic_name


