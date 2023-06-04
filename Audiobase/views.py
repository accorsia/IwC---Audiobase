from django.http import Http404
from django.shortcuts import render
from .models import Artist, Album


def artist_to_dict(artist):
    artist_dict = {
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
    return artist_dict


def album_to_dict(album):
    album_dict = {
        'idb': album.idb,
        'ida': album.ida,
        'bname': album.bname,
        'year': album.year,
        'genre': album.genre,
        'gold': album.gold,
        'plat': album.plat,

        # 'songs': album.song_set.all()
    }
    return album_dict


# Create your views here.
def index(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    return render(request, 'Audiobase/index.html', {'artists': artists, 'albums': albums})


"""def artist_bio(request, artist_id):


    context = artist_to_dict(Artist.objects.get(ida=artist_id))
    return render(request, 'Audiobase/artist.html', context)"""

def artist_bio(request, artist_id):
    try:
        artist_obj = Artist.objects.get(ida=artist_id)
    except Artist.DoesNotExist:
        raise Http404("L'artista non esiste")

    albums = Album.objects.filter(ida=artist_obj)

    context = {
        'artist': artist_to_dict(artist_obj),
        'albums': artist_obj.album_set.all()
    }
    return render(request, 'Audiobase/artist.html', context)


def album_bio(request, album_id):

    #   Check if album_id's album actually exists
    try:
        album_obj = Album.objects.get(idb=album_id)
    except Album.DoesNotExist:
        raise Http404("L'album non esiste")

    context = {'album': album_to_dict(album_obj),
               'songs': album_obj.song_set.all()}
    return render(request, 'Audiobase/album.html', context)
