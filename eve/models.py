from django.db import models


# Create your models here.
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=500, default="No remark provided")
    cloudUrl = models.CharField(max_length=200, default='', null=True, blank=True)
    prediction = models.IntegerField(default=2)

    def __str__(self):
        return self.file.name
