from django.db import models

# Create your models here.
class zooBooking(models.Model):
    zooID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    arriveDate = models.DateTimeField()
    leaveDate = models.DateTimeField()
    numAdults = models.IntegerField()
    numChildren = models.IntegerField()
    numInfants = models.IntegerField()

    def __str__(self):
        return self.first_name