from django.db import models
from account.models import User
from category.models import Category
from django.utils.text import slugify
# Create your models here.

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    topic_name = models.CharField('Topic Name', max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('Description', max_length=300)
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.topic_name, allow_unicode=True)
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.topic_name


