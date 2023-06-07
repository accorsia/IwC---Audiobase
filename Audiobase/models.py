import os
from datetime import date
from django.db import models

#   'a' ---> Artist
class Artist(models.Model):
    ida = models.AutoField(primary_key=True)  # primary key

    aname = models.CharField(max_length=100, verbose_name="Name")
    stagename = models.CharField(max_length=100, verbose_name="Stage name")
    birth = models.DateField("Birth")
    age = models.IntegerField(default=0)    # read only
    n_gold = models.IntegerField(default=0, verbose_name="Gold records")  # read only
    n_plat = models.IntegerField(default=0, verbose_name="Platinum records")  # read only
    nation = models.CharField(max_length=100, verbose_name="Nationality")

    artist_image = models.ImageField(null=True, blank=True, upload_to="artist_img/")    # profile pic
    show_ida = models.IntegerField(verbose_name="Ida", null=True, default=-1)

    #   [str] that shows in the dropdown menu
    def __str__(self):
        return str(self.stagename)

    def __repr__(self):
        return f"Artist(ida={self.ida}, aname='{self.aname}', stagename='{self.stagename}', birth={self.birth}, age={self.age}, n_gold={self.n_gold}, n_plat={self.n_plat}, nation='{self.nation}')"


    ####################################################################################################################

    def calculate_certifications(self):
        artist_albums = Album.objects.filter(ida=self)

        self.gold = artist_albums.filter(gold=True).count()
        self.plat = artist_albums.filter(plat=True).count()

    #   Override ---> calculate read only fields
    def save(self, *args, **kwargs):
        self.calculate_certifications()
        self.age = date.today().year - self.birth.year

        if self.ida is not None:
            self.show_ida = self.ida
        else:
            self.show_ida = -1

        super().save(*args, **kwargs)


#   'b' ---> Album
class Album(models.Model):
    idb = models.AutoField(primary_key=True)  # primary key

    ida = models.ForeignKey(Artist, on_delete=models.CASCADE)  # foreign key, read only
    artist_name = models.CharField(max_length=100, verbose_name="Artist", default="Artist name will appear here...")    # read only
    bname = models.CharField(max_length=100, verbose_name="Name")
    year = models.IntegerField(verbose_name="Release year")
    genre = models.CharField(max_length=100)
    gold = models.BooleanField(verbose_name="Gold record")
    plat = models.BooleanField(verbose_name="Platinum record")

    album_image = models.ImageField(null=True, blank=True, upload_to="album_img/")  # album cover
    show_idb = models.IntegerField(verbose_name="Idb", null=True, default=-1)

    def __str__(self):
        return self.bname

    ####################################################################################################################

    #   Override --> calculate: 'artist_name', 'ida'
    def save(self, *args, **kwargs):
        #   artist_name
        artist = Artist.objects.get(ida=self.ida_id)
        self.artist_name = artist.stagename

        #   ida
        self.ida = artist
        #   ...OPPURE...
        #   self.ida_id = artist.ida

        if self.idb is not None:
            self.show_idb = self.idb
        else:
            self.show_idb = -1

        super().save(*args, **kwargs)

#   's' ---> Song
class Song(models.Model):
    ids = models.AutoField(primary_key=True)  # primary key

    idb = models.ForeignKey(Album, on_delete=models.CASCADE)  # foreign key
    sname = models.CharField(max_length=100, verbose_name="Name")
    artist_name = models.CharField(max_length=100, verbose_name="Artist", default="Artist name will appear here...")    # read only
    album_name = models.CharField(max_length=100, verbose_name="Album", default="Album name will appear here...")   # read only
    pubdate = models.IntegerField(verbose_name="Release year", default=0)   # read only
    length = models.IntegerField(verbose_name="Length in [seconds]")
    spoty_str = models.IntegerField(verbose_name="Thousands of streams [x1000]")

    def __str__(self):
        return self.sname

    ####################################################################################################################

    #   Override --> calculate: 'album_name', 'pubdate', 'artist_name'
    def save(self, *args, **kwargs):
        #   album_name, pubdate
        album = Album.objects.get(idb=self.idb_id)
        self.album_name = album.bname
        self.pubdate = album.year

        #   artist_name
        artist = Artist.objects.get(ida=album.ida_id)
        self.artist_name = artist.stagename

        #   idb
        self.idb = album

        super().save(*args, **kwargs)

