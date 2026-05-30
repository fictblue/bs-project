from django.shortcuts import render
from django.http import JsonResponse
from .models import AIMemory, AIConversation
from members.models import Member
from events.models import Event
from lore.models import Lore
from django.conf import settings
from groq import Groq
import json


def build_system_prompt():
    """Build system prompt dari data DB terkini."""

    memories = AIMemory.objects.all()
    context = "\n".join([f"{m.key}: {m.content}" for m in memories]) or "Belum ada memory."

    members = Member.objects.all()
    member_info = "\n".join([
        f"- {m.nickname} ({m.real_name}) | role: {m.get_role_display()} | status: {m.get_status_display()} | skills: {m.skills or '-'} | fav game: {m.favorite_game or '-'}"
        for m in members
    ]) or "Belum ada data member."

    events = Event.objects.filter(status='upcoming').order_by('date')[:5]
    event_info = "\n".join([
        f"- {e.title} | {e.date.strftime('%d %B %Y, %H:%M')} | {e.location}"
        for e in events
    ]) or "Tidak ada event upcoming."

    lores = Lore.objects.all().order_by('-created_at')[:10]
    lore_info = "\n".join([
        f"- [{l.get_category_display()}] {l.title}: {l.content[:200]}"
        for l in lores
    ]) or "Belum ada lore."

    return f"""Kamu adalah AI BS Assistant — asisten virtual tongkrongan Baraya Salawasna (BS).

Kepribadianmu:
- Santai, lucu, dan gak kaku
- Kadang nyindir tapi tetap sopan, gak brutal
- Ngerti semua lore dan inside joke BS
- Pakai bahasa gaul Indonesia yang natural (lo/gue, bro, dll)
- Kalau ditanya hal yang lo gak tau, jawab dengan jujur tapi tetap santai dan lucu
- Jawaban singkat dan padat — jangan panjang kalau gak perlu

Data BS yang lo tau:

[MEMORIES & INSIDE JOKES]
{context}

[MEMBER-MEMBER BS]
{member_info}

[EVENT UPCOMING]
{event_info}

[LORE BS]
{lore_info}"""


def ai_chat(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            user_message = body.get('message', '').strip()
            history = body.get('history', [])

            if not user_message:
                return JsonResponse({'error': 'Pesan kosong.'}, status=400)

            # Bangun messages payload
            messages_payload = [{'role': 'system', 'content': build_system_prompt()}]
            for h in history[-10:]:
                if h.get('role') in ('user', 'assistant') and h.get('content'):
                    messages_payload.append({'role': h['role'], 'content': h['content']})
            messages_payload.append({'role': 'user', 'content': user_message})

            client = Groq(api_key=settings.GROQ_API_KEY)
            response = client.chat.completions.create(
                model='llama-3.1-8b-instant',
                messages=messages_payload,
                max_tokens=600,
                temperature=0.85,
            )
            ai_response = response.choices[0].message.content

            # Simpan ke DB
            AIConversation.objects.create(
                user_message=user_message,
                ai_response=ai_response,
            )

            return JsonResponse({'response': ai_response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'ai_assistant/ai_chat.html')