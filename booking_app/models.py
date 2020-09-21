from django.db import models

# Create your models here.

class bookingSpace(models.Model):
    fullname = models.CharField(max_length=150)
    busStop = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return '{} made a request'.format(self.fullname)
    
