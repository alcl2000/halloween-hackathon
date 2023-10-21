from django.db import models
from django.contrib.auth.models import User
from costumes.models import Costume


class Vote(models.Model):
    """
    Vote model, related to 'owner' and 'costume post'.
    'owner' is a User instance and 'costume post' is a Costume instance.
    'unique_together' makes sure a user can't vote the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Costume, related_name='votes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'