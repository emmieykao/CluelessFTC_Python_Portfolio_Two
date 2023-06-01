from django.shortcuts import render, redirect
from django.db import connection, connections
# from MusicDatabase.models import Artist

def index(request):
    sqlQuery = "SELECT artist.id, artist.Name, artist.Formed, artist.website FROM artist ORDER BY artist.Formed asc"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close()
    
    return render(request, "MusicDatabase/index.html", {
        "artists":rows
    })

def indexWithSort(request, sort):
    if sort in ["name", "id", "formed"]:
        sqlQuery = f"SELECT artist.id, artist.Name, artist.Formed, artist.website FROM artist ORDER BY artist.{sort} asc"
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            rows = list(cursor.fetchall())
            cursor.close()
            connection.close()
    
        return render(request, "MusicDatabase/index.html", {
        "artists":rows
    })

def ArtistsSongs(request, sID):
    sqlQuery = "SELECT track.AlbumID, track.TrackID, track.TrackName, track.TrackLength, album.AlbumName FROM album "
    sqlQuery += "INNER JOIN track ON album.id = track.AlbumID WHERE album.id = " + str(sID) + " ORDER BY track.TrackLength asc"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery) 
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close()

    return render(request, "MusicDatabase/song.html", {
    "songs":rows})

def ArtistsAlbums(request, aID):
    sqlQuery = "SELECT artist.id, album.id, artist.Name, album.AlbumName, album.YearReleased FROM artist "
    sqlQuery += "INNER JOIN album ON artist.id = album.ArtistID WHERE artist.id = " + str(aID) + " ORDER BY album.YearReleased asc"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery) 
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close()

    return render(request, "MusicDatabase/album.html", {
    "albums":rows
    })