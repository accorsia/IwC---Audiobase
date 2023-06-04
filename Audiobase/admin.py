from django.contrib import admin
from .models import Album, Artist, Song


# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = ('age',)


class SongAdmin(admin.ModelAdmin):
    readonly_fields = ("artist_name", "album_name", 'pubdate')


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ("artist_name", )


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)

# admin.site.register(Album)
# admin.site.register(Song)
# admin.site.register(Artist)
