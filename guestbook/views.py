from django.shortcuts import render

from .models import GuestEntry

def index(request):
    entries = GuestEntry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'guestbook/index.html', {'entries': entries})
