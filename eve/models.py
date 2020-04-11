import uuid
from django.db import models


# Create your models here.
class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=500, default="No remark provided")
    cloudUrl = models.CharField(max_length=200, default='Not uploaded to cloud', null=True, blank=True)
    prediction = models.IntegerField(default=-1)
    isCorrect = models.BooleanField(default=None, blank=True, null=True)
    userSuggestion = models.IntegerField(default=-1)

    def __str__(self):
        return self.file.name
