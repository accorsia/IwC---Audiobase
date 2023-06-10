from django.http import Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Artist, Album

# Create your views here.
def index(request):

    #   Check database status
    try:
        artists_obj = Artist.objects.all()
    except Artist.DoesNotExist:
        raise Http404("Nessun artista disponibile")

    try:
        albums_obj = Album.objects.all()
    except Album.DoesNotExist:
        raise Http404("Nessun album disponibile")

    context = {
        'artists': artists_obj,
        'albums': albums_obj
    }

    return render(request, 'Audiobase/index.html', context)


def artist_bio(request, artist_id):
    #   Check if 'artist_id' artist actually exists
    try:
        artist_obj = Artist.objects.get(ida=artist_id)
    except Artist.DoesNotExist:
        raise Http404("L'artista non esiste")

    #   update object before showing its data
    artist_obj.update()

    context = {
        'artist': artist_obj,
        'albums': artist_obj.album_set.all(),
    }
    return render(request, 'Audiobase/artist.html', context)


def album_bio(request, album_id):
    #   Check if 'album_id' album actually exists
    try:
        album_obj = Album.objects.get(idb=album_id)
    except Album.DoesNotExist:
        raise Http404("L'album non esiste")

    context = {
        'album': album_obj,
        'songs': album_obj.song_set.all(),
    }
    return render(request, 'Audiobase/album.html', context)

def vote_album(request):

    if request.method == 'POST':

        selected_album_id = request.POST.get('best_album')  #   album.idb
        selected_album = get_object_or_404(Album, idb=selected_album_id)

        #   album database update
        selected_album.best_album += 1
        selected_album.save()

        #   success message in the admin interface
        messages.success(request, "Voto registrato!")

        return HttpResponseRedirect(reverse('ab:album_bio', args=[selected_album_id]))

    #   wrong method: GET
    else:
        return HttpResponseBadRequest

def results(request):

    #   whole database
    albums = Album.objects.all()
    artists = Artist.objects.all()

    return render(request, 'Audiobase/results.html', {'albums': albums, 'artists':artists})