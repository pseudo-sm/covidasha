from django.db import models

# Create your models here.

class Alert(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    want = models.BooleanField()
    what = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + self.what

class Enquiry(models.Model):

    alert = models.ForeignKey(Alert,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
