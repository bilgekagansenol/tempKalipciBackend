from django.db import models

class DownloadCounter(models.Model):
    name = models.CharField(max_length=200, unique=True, default='default')
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.count}"

    class Meta:
        verbose_name = 'Download Counter'
        verbose_name_plural = 'Download Counters'
