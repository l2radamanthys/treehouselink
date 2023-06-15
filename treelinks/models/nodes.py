from django.db import models
from django.contrib.auth.models import User


class Node(models.Model):
    user = models.ForeignKey(User, related_name="nodes", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="default", blank=False, null=False)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'nodes'
        verbose_name = "Node"
        verbose_name_plural = "Nodes"

    def __str__(self):
        return self.name
