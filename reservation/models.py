from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    #times = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    time = models.DateTimeField()
    ppl = (
        ('2', '3'),
        ('3', '4'),
        ('4', '5'),
        ('5', '6'),
        ('6', '7'),
        ('7', '8')
    )
    party = models.CharField(max_length=10, choices=ppl)
    
    def __str__(self):
        return f'{self.name} booked a table for {self.party} people at {self.time} o clock'