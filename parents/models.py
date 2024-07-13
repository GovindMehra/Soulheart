from django.db import models
from django.contrib.auth.models import User

class Chore(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chores')
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Star(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stars')
    chore = models.OneToOneField(Chore, on_delete=models.CASCADE, related_name='star')
    awarded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.chore.title}'

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('parent', 'Parent'),
        ('kid', 'Kid'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.user_type}'