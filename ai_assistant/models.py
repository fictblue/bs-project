from django.db import models


class AIMemory(models.Model):
    CATEGORY_CHOICES = [
        ('lore', 'Lore'),
        ('quote', 'Quote'),
        ('inside_joke', 'Inside Joke'),
        ('member_info', 'Member Info'),
        ('event_info', 'Event Info'),
    ]
    
    key = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.key


class AIConversation(models.Model):
    user_message = models.TextField()
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_message[:50]
