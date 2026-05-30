from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from members.models import Member
from gallery.models import Gallery
from events.models import Event
from lore.models import Lore
from ai_assistant.models import AIMemory


@login_required
def dashboard(request):
    context = {
        'total_members': Member.objects.count(),
        'total_photos': Gallery.objects.count(),
        'total_events': Event.objects.count(),
        'total_lores': Lore.objects.count(),
        'total_ai_memories': AIMemory.objects.count(),
        'recent_members': Member.objects.all()[:5],
        'recent_photos': Gallery.objects.all()[:5],
        'upcoming_events': Event.objects.filter(status='upcoming')[:5],
    }
    return render(request, 'dashboard/dashboard.html', context)
