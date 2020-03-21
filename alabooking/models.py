from django.db import models

# Create your models here.
"""class Customer(models.Model):
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add = True, null=True)

    def __str__(self):
        return self.name
"""

class Room(models.Model):
    AVAILABILITY = (
        ('Available', 'Available'),
        ('Booked', 'Booked'),
    )
    name = models.CharField(max_length = 200, null = True)
    description = models.CharField(max_length = 200, null = True)
    availability = models.CharField(max_length = 200, null = True, choices = AVAILABILITY)
    date_created = models.DateTimeField(auto_now_add = True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    #customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    room = models.ForeignKey(Room, null = True, on_delete = models.SET_NULL)
    reason = models.CharField(null=True, max_length=50)
    dateToBeUsed = models.DateTimeField(null = True)
    timeToBeUsedFrom = models.DateTimeField(null=True)
    timeToBeUsedTo = models.DateTimeField(null=True)
    status = models.CharField(max_length = 200, null = True, choices = STATUS)
    date_created = models.DateTimeField(auto_now_add = True, null=True)
