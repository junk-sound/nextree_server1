from django.db import models
from account.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField('Category', max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True,help_text='one word for title alias.')

    class Meta:
        ordering = ['category_name']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.category_name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

