from django.db import models
from django.utils import timezone


class DailyQuote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.quote[:50]
