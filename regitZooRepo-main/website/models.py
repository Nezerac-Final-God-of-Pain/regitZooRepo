from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ZooBooking(models.Model):
    BOOKING_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    PLACE_TYPE_CHOICES = [
        ('hotel', 'Hotel'),
        ('zoo', 'Zoo'),
    ]

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_type = models.CharField(
        max_length=10,
        choices=PLACE_TYPE_CHOICES,
        default='hotel'
    )
    visit_date = models.DateField()
    adult_tickets = models.IntegerField(default=1)
    child_tickets = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='pending')
    booking_date = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        adult_price = 40.00
        child_price = 26.50
        return (self.adult_tickets * adult_price) + (self.child_tickets * child_price)

    def __str__(self):
        return f'Booking #{self.booking_id} - {self.user.username} - {self.visit_date}'

    class Meta:
        ordering = ['-booking_date']
