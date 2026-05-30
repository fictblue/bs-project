from django.db import models


class Event(models.Model):
    CATEGORY_CHOICES = [
        ('karangtaruna', 'Karangtaruna'),
        ('mabar', 'Mabar'),
        ('lomba', 'Lomba'),
        ('rapat', 'Rapat'),
        ('volunteer', 'Volunteer'),
    ]
    
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='mabar')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    participants = models.TextField(blank=True, help_text="Separate with commas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date']
