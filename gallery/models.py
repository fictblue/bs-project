from django.db import models


class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('event', 'Event'),
        ('mabar', 'Mabar'),
        ('random', 'Random'),
        ('nostalgia', 'Nostalgia'),
    ]
    
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='gallery/')
    caption = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='random')
    event_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
