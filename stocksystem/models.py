from django.db import models



#Choices
Book_Category = (
    ('finance', 'Finance'),
    ('management', 'Management'),
    ( 'engineering','Engineering'),
    ( 'design' , 'Design'),
    ('arts_and_music','Arts & Music'),
    ('it_&_computers' , 'Information Technology'),)

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(verbose_name='Bio')
    dob       = models.DateField()
    address   = models.CharField(max_length=255)
    country   = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book (models.Model):
    '''class to describe all books collection'''
    isbn_number = models.CharField(max_length=150)
    title       = models.CharField(max_length=255)
    description = models.TextField()
    author      = models.ManyToManyField(Author)
    category    = models.CharField(max_length=255,choices=Book_Category)

    def __str__(self):
        return self.title






class Inventory(models.Model):
    pass
    class Meta:
        verbose_name_plural = 'Inventory'




