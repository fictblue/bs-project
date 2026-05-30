from django.db import models


class Lore(models.Model):
    CATEGORY_CHOICES = [
        ('quote', 'Quote Legendaris'),
        ('event', 'Kejadian Absurd'),
        ('meme', 'Meme Internal'),
        ('history', 'Sejarah BS'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date_occurred = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_occurred', '-created_at']
