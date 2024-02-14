from django.db import models
from django.contrib.auth.models import User


class Adventure(models.Model):
    """
    Adventure model, related to User only, belongs to the owner.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    adv_type = models.CharField(max_length=255)
    personal_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content