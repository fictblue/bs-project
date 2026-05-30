from django.shortcuts import render
from .models import DailyQuote
from members.models import Member
from gallery.models import Gallery
from lore.models import Lore
import random


def homepage(request):
    # Get random quote
    quotes = list(DailyQuote.objects.all())
    random_quote = random.choice(quotes) if quotes else {"quote": "Tongkrongan aktif sejak manusia masih waras.", "author": "BS Legend"}
    
    # Get stats
    total_members = Member.objects.count()
    total_photos = Gallery.objects.count()
    active_members = Member.objects.filter(status='active').count()
    
    # Get gallery photos for slideshow
    gallery_photos = list(Gallery.objects.all()[:10])
    
    # Get recent lore entries
    recent_lores = list(Lore.objects.all()[:3])
    
    # Get talent data from members
    members = Member.objects.filter(status='active')
    talents = {}
    
    for member in members:
        if member.skills:
            skill_list = [s.strip().lower() for s in member.skills.split(',')]
            for skill in skill_list:
                if skill:
                    talents[skill] = talents.get(skill, 0) + 1
    
    # Sort talents by count
    sorted_talents = sorted(talents.items(), key=lambda x: x[1], reverse=True)
    
    # Timeline data (hardcoded for now since it's rare updates)
    timeline = [
        {'year': '2018', 'title': 'BS Terbentuk', 'description': 'Awal dari segalanya.'},
        {'year': '2020', 'title': 'Karang Taruna', 'description': 'Mulai aktif di kegiatan karang taruna.'},
        {'year': '2022', 'title': 'Turnamen Pertama', 'description': 'Partisipasi pertama di turnamen.'},
        {'year': '2024', 'title': 'Perubahan', 'description': 'Beberapa anggota mulai bekerja dan berkeluarga.'},
        {'year': '2026', 'title': 'Website BS', 'description': 'Website resmi BS dibuat.'},
    ]
    
    context = {
        'random_quote': random_quote,
        'total_members': total_members,
        'total_photos': total_photos,
        'active_members': active_members,
        'gallery_photos': gallery_photos,
        'recent_lores': recent_lores,
        'talents': sorted_talents[:8],  # Top 8 talents
        'timeline': timeline,
    }
    return render(request, 'core/homepage.html', context)
