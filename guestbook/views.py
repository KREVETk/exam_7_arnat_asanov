from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import GuestEntryForm, SearchForm
from .models import GuestEntry

def index(request):
    entries = GuestEntry.objects.filter(status='active').order_by('-created_at')
    form = SearchForm(request.GET)

    if form.is_valid() and form.cleaned_data['name']:
        entries = entries.filter(name__icontains=form.cleaned_data['name'])

    entry_form = GuestEntryForm()

    return render(request, 'guestbook/index.html', {
        'entries': entries,
        'search_form': form,
        'entry_form': entry_form
    })

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

def delete_entry(request, pk):
    entry = get_object_or_404(GuestEntry, pk=pk)

    if request.method == 'POST':
        email_input = request.POST.get('email')
        if email_input == entry.email:
            entry.delete()
            messages.success(request, 'Запись удалена.')
            return redirect('index')
        else:
            messages.error(request, 'Email не совпадает. Удаление не выполнено.')

    return render(request, 'guestbook/delete_entry.html', {'entry': entry})