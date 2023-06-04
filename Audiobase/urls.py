from django.urls import path
from . import views

#   mapping URL <-> funzioni in 'views.py'
urlpatterns = \
[
    path('', views.index, name='index'),                                    #   localhost/ab/
    path('artists/<int:artist_id>', views.artist_bio, name='artist_bio'),    #   localhost/ab/artists/ida
    path('albums/<int:album_id>', views.album_bio, name='album_bio')               #   localhost/ab/albums/idb
]