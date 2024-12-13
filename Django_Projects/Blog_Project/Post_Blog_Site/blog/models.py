from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# Post model class
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    pubished_date = models.DateTimeField(blank=True,null=True)

    # Function to set publish date for a post
    def publish(self):
        self.pubished_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    # once blog post added, redirect to blog post detail page with primary key
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title
    
# Comment model class
class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    # Function to approve the comment for post
    def approve(self):
        self.approved_comment = True
        self.save()

    # Once saved comments, return/re-direct to blog post listing page 
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
