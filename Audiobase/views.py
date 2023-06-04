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
    }
    return artist_dict
def album_to_dict(album):
    album_dict = {
        'idb': album.idb,
        'ida': album.ida.ida,
        'bname': album.bname,
        'year': album.year,
        'genre': album.genre,
        'gold': album.gold,
        'plat': album.plat,
    }
    return album_dict


# Create your views here.
def index(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    return render(request, 'Audiobase/index.html', {'artists': artists, 'albums': albums})



def artist_bio(request, artist_id):
    context = artist_to_dict(Artist.objects.get(ida=artist_id))
    return render(request, 'Audiobase/artist.html', context)


def album_bio(request, album_id):
    context = album_to_dict(Album.objects.get(idb=album_id))
    return render(request, 'Audiobase/album.html', context)
