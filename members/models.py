from django.db import models


class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name


class Member(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('legend', 'Legend'),
    ]
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('alumni', 'Alumni'),
    ]
    
    nickname = models.CharField(max_length=100, unique=True)
    real_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    skills = models.TextField(help_text="Separate with commas")
    favorite_game = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='members/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    badges = models.ManyToManyField(Badge, blank=True)
    instagram = models.CharField(max_length=100, blank=True, help_text="Instagram username (without @)")
    tiktok = models.CharField(max_length=100, blank=True, help_text="TikTok username (without @)")
    whatsapp = models.CharField(max_length=20, blank=True, help_text="WhatsApp number (with country code)")
    join_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nickname
    
    class Meta:
        ordering = ['-created_at']
