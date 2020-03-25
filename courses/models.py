from django.db import models

# Create your models here.

class Course(models.Model):
    """Model class for Course"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string representation of the Course object"""
        return self.title

    class Meta:
        ordering = ['title',]
    #Check on repr for test driven development
    """def __repr__(self):
        return Course.__name__"""