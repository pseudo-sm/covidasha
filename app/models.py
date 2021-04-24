from django.db import models
from datetime import datetime
# Create your models here.
from pytz import utc


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

    @property
    def get_duration(self):
        now = datetime.utcnow().replace(tzinfo=utc)
        duration = now - self.datetime
        print(self.datetime,now)
        print(duration.days,duration.seconds)
        if duration.days == 0:
            if duration.seconds / 3600 < 1:
                return str(int(duration.seconds / 60)) + " minutes"
            elif duration.days < 1:
                return str(int(duration.seconds / 3600)) + " hours"
        else:
            return str(int(duration.days)) + " days"


class Enquiry(models.Model):

    alert = models.ForeignKey(Alert,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
