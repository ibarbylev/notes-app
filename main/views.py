from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView

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


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title',  'image_url', 'content']
    template_name = 'note-edit.html'
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['title'] = 'Edit page'
    #     note = context['note']
    #     # context['heading_text'] = f'Creating of {note.doc_name}'
    #     # context['description'] = f'On this page you can update the document {note.doc_name}.'
    #     return context


class NoteDeleteView(DeleteView):
    model = Note
    fields = ['title',  'image_url', 'content']
    template_name = 'note-delete.html'
    success_url = reverse_lazy('index')


class NoteDetailView(DetailView):
    model = Note
    fields = ['title',  'image_url', 'content']
    template_name = 'note-details.html'
    success_url = reverse_lazy('index')

