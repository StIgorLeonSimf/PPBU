from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.name
