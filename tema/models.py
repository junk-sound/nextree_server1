from django.db import models
# from django.contrib.auth.models import User
from account.models import User
from topic.models import Topic
from django.utils.text import slugify
# Create your models here.

class Tema(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    tema_name = models.CharField('TEMA', max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    order_num = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.tema_name, allow_unicode=True)
        super(Tema, self).save(*args, **kwargs)

    def __str__(self):
        return self.tema_name

