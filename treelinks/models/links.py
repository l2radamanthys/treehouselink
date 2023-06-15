from django.db import models


class Link(models.Model):
    node = models.ForeignKey("Node", related_name="links", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    uri = models.CharField(max_length=500, default="https://", blank=False, null=False)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'links'
        verbose_name = "Link"
        verbose_name_plural = "links"

    def __str__(self):
        return self.name 
