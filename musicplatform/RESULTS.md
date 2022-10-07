python manage.py shell

<!-- create some artists -->

from artists.models import Artist
>>> addArtist=Artist(Stage_name="drake",Social_link="https://www.instagram.com/drake/")
>>> addArtist.save()
>>> addArtist=Artist(Stage_name="max",Social_link="https://www.instagram.com/drake/")
>>> addArtist.save()
>>> addArtist=Artist(Stage_name="mazen",Social_link="https://www.instagram.com/drake/")
>>> addArtist.save()

<!-- list down all artists -->

>>> Artist.objects.all()
<QuerySet [<Artist: Ahmed>, <Artist: drake>, <Artist: max>, <Artist: mazen>]>

<!-- list down all artists sorted by name -->

>>> Artist.objects.all().order_by('Stage_name')
<QuerySet [<Artist: Ahmed>, <Artist: drake>, <Artist: max>, <Artist: mazen>]>

<!-- list down all artists whose name starts with `a` -->

>>> Artist.objects.filter(Stage_name__startswith='a')|Artist.objects.filter(Stage_name__startswith='A')         
<QuerySet [<Artist: Ahmed>]>

<!-- in 2 different ways, create some albums and assign them to any artists -->

>>> from albums.models import Album
>>> import datetime
>>> art=Artist.objects.get(id=1)
>>> alb=Album()
>>> alb.name='fav album'
>>> alb.release_datetime=datetime.date(2022,10,30)
>>> alb.cost=50.60
>>> alb.artist=art
>>> alb.save()


>>> art=Artist.objects.get(id=1)
>>> alb=Album()
>>> alb.name='lose album'
>>> alb.release_datetime=datetime.date(2022,10,29)
>>> alb.cost=55.60
>>> alb.artist=art
>>> alb.save()

>>> art=Artist.objects.get(id=2) 
>>> alb=Album.objects.create(name='max album',release_datetime=datetime.date(2022,10,1),cost=12.30,artist=art)

>>> art=Artist.objects.get(id=3) 
>>> alb=Album.objects.create(name='morning album',release_datetime=datetime.datetime(2022, 10, 4, 23, 55, 59, 342380),cost=18.30,artist=art)

<!-- get the latest released album -->

>>> Album.objects.latest('release_datetime')
<Album: fav album>

<!-- get all albums released before today -->

>>> Album.objects.filter(release_datetime__lt=datetime.date.today()) 
<QuerySet [<Album: max album>, <Album: morning album>]>

<!-- get all albums released today or before but not after today -->

>>> Album.objects.filter(release_datetime__lte=datetime.date.today())  
<QuerySet [<Album: max album>, <Album: morning album>]>

<!-- count the total number of albums -->

>>> Album.objects.count()
4

<!-- in 2 different ways, for each artist, list down all of his/her albums -->

>>> for artist in Artist.objects.all():
...          print(artist , Album.objects.filter(artist_id=artist.id))  
... 
Ahmed <QuerySet []>
drake <QuerySet [<Album: fav album>, <Album: lose album>]>
max <QuerySet [<Album: max album>]>
mazen <QuerySet [<Album: morning album>]>


>>> for artist in Artist.objects.all():
...           print(artist ,artist.album_set.all())
... 
Ahmed <QuerySet []>
drake <QuerySet [<Album: fav album>, <Album: lose album>]>
max <QuerySet [<Album: max album>]>
mazen <QuerySet [<Album: morning album>]>


<!--list down all albums ordered by cost then by name-->

>>> Album.objects.order_by('cost','name')
<QuerySet [<Album: max album>, <Album: morning album>, <Album: fav album>, <Album: lose album>]>
