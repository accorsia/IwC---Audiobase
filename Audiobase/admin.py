from django.contrib import admin

from .models import Album, Artist, Song


# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = ('age', 'n_gold', 'n_plat', 'show_ida')

    fieldsets = (
        ('Input', {
            'fields': ('aname', 'stagename', 'birth', 'nation', 'artist_image'),
        }),
        ('ReadOnly', {
            'fields': readonly_fields,
            # 'classes': ('collapse',),
        }),
    )


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('artist_name', 'show_idb', 'best_album')

    fieldsets = (
        ('Input', {
            'fields': ('ida', 'bname', 'year', 'genre', 'gold', 'plat', 'album_image'),
        }),
        ('ReadOnly', {
            'fields': readonly_fields,
            # 'classes': ('collapse',),
        }),
    )


class SongAdmin(admin.ModelAdmin):
    readonly_fields = ('artist_name', 'album_name', 'pubdate')

    fieldsets = (
        ('Input', {
            'fields': ('idb', 'sname', 'length', 'spoty_str'),
        }),
        ('ReadOnly', {
            'fields': readonly_fields,
            # 'classes': ('collapse',),
        }),
    )


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)

# admin.site.register(Album)
# admin.site.register(Song)
# admin.site.register(Artist)
