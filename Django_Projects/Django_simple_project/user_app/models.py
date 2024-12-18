from django.db import models

# Create your models here.
class Author_class(models.Model):
    author_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.author_name
    
class Book_class(models.Model):
    book_author_name = models.ForeignKey(Author_class, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=264)

    def __str__(self):
        return self.book_name

class Book_published(models.Model):
    book_name = models.ForeignKey(Book_class,on_delete=models.CASCADE)
    book_date_published = models.DateField()

    def __str__(self):
        return self.book_date_published
