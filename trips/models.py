from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):
    """
    Model for posting items need for a trip.
    """
    buy_needed = [
        ('y', 'Y'),
        ('n', 'N'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    buy = models.CharField(
        max_length=255,
        choices=buy_needed,
        null=True, blank=True,
        default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.quantity} {self.buy}"

    class Meta:
        ordering = ['-buy']
