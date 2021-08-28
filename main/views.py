from django.shortcuts import render, redirect

from notes.forms import NoteForm, ProfileForm
from notes.models import Profile, Note


def show_profile_or_list_of_notes(request):
    is_profile_data = Profile.objects.exists()
    if is_profile_data:
        profile = Profile.objects.last()
        is_notes = Note.objects.exists()
        notes = []
        if is_notes:
            notes = Note.objects.all()
        context = {'is_notes': is_notes,
                   'notes': notes,
                   'profile': profile,
                   'notes_form': NoteForm()}
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == 'POST':
            profile = ProfileForm(request.POST)
            if profile.is_valid():
                profile.save()
            return redirect('index')
        else:
            context = {'form': ProfileForm()}
            return render(request, 'home-no-profile.html', context)


def create_note_view(request, **kwargs):
    if request.method == "POST":
        profile = Profile.objects.last()
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.profile_id = profile
            print(type(profile))
            print(profile)
            note.save()
            return redirect('index')
        else:
            context = {'form': NoteForm(request.POST)}
            return render(request, 'note-create.html', context)

    context = {'form': NoteForm()}
    return render(request, 'note-create.html', context)


