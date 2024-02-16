from django.db import models
from django.contrib.auth.models import User


class Adventure(models.Model):
    """
    Adventure model, related to User only, belongs to the owner.
    """
    activity_choices = [
        ('family', 'Family'),
        ('hobbies', 'Hobbies'),        
        ('sport', 'Sport'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    activity = models.CharField(
        max_length=255,
        choices=activity_choices,
        null=True, blank=True,
        default='other')
    personal_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rxxwye', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'