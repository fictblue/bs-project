from django.shortcuts import render
from .models import Event


def event_list(request):
    events = Event.objects.all()
    status_filter = request.GET.get('status')
    
    if status_filter:
        events = events.filter(status=status_filter)
    
    context = {
        'events': events,
        'status_filter': status_filter,
    }
    return render(request, 'events/event_list.html', context)


def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    participants_list = event.participants.split(',') if event.participants else []
    context = {
        'event': event,
        'participants_list': participants_list,
    }
    return render(request, 'events/event_detail.html', context)
