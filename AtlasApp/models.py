from django.db import models

class Reservation(models.Model):
    phone_number = models.CharField(max_length=15)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'Reservation - Phone: {self.phone_number}, Date: {self.date_time}'
