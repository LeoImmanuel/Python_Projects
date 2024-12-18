from django.db import models

# Create your models here.
class Topic_class(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic_name

class Web_page_class(models.Model):
    webpage_topic = models.ForeignKey(Topic_class, on_delete=models.CASCADE)
    webpage_name = models.CharField(max_length=264, unique=True)
    webpage_url = models.URLField(unique=True)

    def __str__(self):
        return self.webpage_name

class Web_Access_Record(models.Model):
    web_access_record_name = models.ForeignKey(Web_page_class, on_delete=models.CASCADE)
    access_date = models.DateField()

    def __str__(self):
        return str(self.access_date)
