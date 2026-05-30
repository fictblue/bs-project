from django.db import models


class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('mvp_sports', 'MVP Olahraga'),
        ('raja_mabar', 'Raja Mabar'),
        ('legend', 'Legend Tongkrongan'),
        ('chaotic', 'Most Chaotic Member'),
        ('talent', 'Talent Showcase'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    recipient = models.CharField(max_length=100)
    date_achieved = models.DateField()
    icon = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.recipient}"
    
    class Meta:
        ordering = ['-date_achieved']
