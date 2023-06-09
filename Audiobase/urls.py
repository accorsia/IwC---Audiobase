from django.urls import path
from . import views

app_name = 'ab' # namespace?

#   mapping URL <-> funzioni in 'views.py'
urlpatterns = \
    [
        #   localhost/ab/
        path('', views.index, name='index'),

        #   localhost/ab/artists/ida
        path('artists/<int:artist_id>', views.artist_bio, name='artist_bio'),

        #   localhost/ab/albums/idb
        path('albums/<int:album_id>', views.album_bio, name='album_bio'),

        path('vote_album/<int:album_id>/', views.vote_album, name='vote_album'),

    ]
