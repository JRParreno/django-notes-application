from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddNoteForm
from django.contrib.auth.models import User


def add_note_view(request):
    author = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = author
            note.save()
            return redirect('home')
    else:
        form = AddNoteForm(instance=author)
    return render(request, 'note/add-note.html', {"form": form})
