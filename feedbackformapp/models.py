from django.db import models
class FeedBackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateField(max_length=100)
    feedback=models.CharField(max_length=100)


