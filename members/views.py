from django.shortcuts import render, get_object_or_404
from .models import Member


def member_list(request):
    members = Member.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'members/member_list.html', context)


def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    skills_list = member.skills.split(',') if member.skills else []
    context = {
        'member': member,
        'skills_list': skills_list,
    }
    return render(request, 'members/member_detail.html', context)
