from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone

class Tip(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    code = models.TextField(max_length=2048)
    source = models.URLField(max_length=256, null=True, default=None)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title
