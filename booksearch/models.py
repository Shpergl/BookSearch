from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="Book Name" )
    author = models.CharField(max_length=100, verbose_name="Author")

    def __str__(self):
        return str(self.name)

class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name="Section Name" )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Page(models.Model):
    text = models.TextField(verbose_name="Page Text" )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

