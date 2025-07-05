from django.shortcuts import render, redirect, get_object_or_404

from .forms import GuestEntryForm
from .models import GuestEntry

def index(request):
    entries = GuestEntry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'guestbook/index.html', {'entries': entries})

def add_entry(request):
    if request.method == 'POST':
        form = GuestEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestEntryForm()
    return render(request, 'guestbook/add_entry.html', {'form': form})

def edit_entry(request, pk):
    entry = get_object_or_404(GuestEntry, pk=pk)
    if request.method == 'POST':
        form = GuestEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestEntryForm(instance=entry)
    return render(request, 'guestbook/edit_entry.html', {'form': form, 'entry': entry})
