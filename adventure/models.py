from django.db import models
from django.contrib.auth.models import User


class Adventure(models.Model):
    """
    Adventure model, related to User only, belongs to the owner.
    """
    activity_filter_choices = [
        ('hiking', 'Hiking'),
        ('cycling', 'Cycling'),
        ('racing', 'Racing'),
        ('rugby', 'Rugby'),
        ('gaa', 'GAA'),
        ('soccer', 'Soccer'),
        ('swimming', 'Swimming'),
        ('climbing', 'Climbing'),
        ('water_sports', 'Water Sports'),
        ('travel', 'Travel'),
        ('running', 'Running'),
        ('other', 'Other'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('running', 'Running'),
        ('other', 'Other')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    personal_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content