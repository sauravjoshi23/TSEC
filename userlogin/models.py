from django.db import models
from django.urls import reverse

class Applicant(models.Model):
    email = models.EmailField() # unique
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    clubs = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    why_aims = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    score = models.IntegerField(default=-1)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('model-detail-view', args=[str(self.id)])
