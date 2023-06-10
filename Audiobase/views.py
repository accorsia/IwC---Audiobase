from django.http import Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Artist, Album


"""def artist_to_dict(artist):
    return {
        'ida': artist.ida,
        'aname': artist.aname,
        'stagename': artist.stagename,
        'birth': artist.birth,
        'age': artist.age,
        'n_gold': artist.n_gold,
        'n_plat': artist.n_plat,
        'nation': artist.nation,

        'albums': artist.album_set.all()  # artist's album list

    }
def album_to_dict(album):
    return {
        'idb': album.idb,
        'ida': album.ida,
        'bname': album.bname,
        'year': album.year,
        'genre': album.genre,
        'gold': album.gold,
        'plat': album.plat,
    }
"""

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
        #'artist_img_path': artists_obj.stagename.replace(" ", "").lower(),
        #'album_img_path':  albums_obj.stagename.replace(" ", "").lower()
    }

    return render(request, 'Audiobase/index.html', context)


def artist_bio(request, artist_id):
    #   Check if 'artist_id' artist actually exists
    try:
        artist_obj = Artist.objects.get(ida=artist_id)
    except Artist.DoesNotExist:
        raise Http404("L'artista non esiste")

    context = {
        'artist': artist_obj,
        'albums': artist_obj.album_set.all(),
        'path_stagename': artist_obj.stagename.replace(" ", "").lower()   #   artist images path in the folder
    }
    return render(request, 'Audiobase/artist.html', context)


def album_bio(request, album_id):
    #   Check if 'album_id' album actually exists
    try:
        album_obj = Album.objects.get(idb=album_id)
    except Album.DoesNotExist:
        raise Http404("L'album non esiste")

    context = {'album': album_obj,
               'songs': album_obj.song_set.all(),
               'path_bname': album_obj.bname.replace(" ", "").lower()   #   album images path in the folder
               }
    return render(request, 'Audiobase/album.html', context)

def vote_album(request):

    if request.method == 'POST':

        selected_album_id = request.POST.get('best_album')
        selected_album = get_object_or_404(Album, idb=selected_album_id)

        selected_album.best_album += 1
        selected_album.save()

        return HttpResponseRedirect(reverse('ab:album_bio', args=[selected_album_id]))

    #   wrong method: GET
    else:
        return HttpResponseBadRequest