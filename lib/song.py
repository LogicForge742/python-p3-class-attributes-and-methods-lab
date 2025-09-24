class Song:
    # Class-level attributes (shared across all Song instances)
    count = 0            # total number of songs created
    genres = []          # unique list of all genres
    artists = []         # unique list of all artists
    genre_count = {}     # dictionary to count songs per genre
    artist_count = {}    # dictionary to count songs per artist

    def __init__(self, name, artist, genre):
        # instance attributes (unique to each song object)
        self.name = name
        self.artist = artist
        self.genre = genre

        # update class-level tracking whenever a new song is created
        Song.add_song_to_count()         # increment song counter
        Song.add_to_genres(genre)        # add genre to list if new
        Song.add_to_artists(artist)      # add artist to list if new
        Song.add_to_genre_count(genre)   # increment genre counter
        Song.add_to_artist_count(artist) # increment artist counter

    @classmethod
    def add_song_to_count(cls, increment=1):
        # increases the total number of songs by 'increment' (default is 1)
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        # ensures no duplicate genres are stored
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # ensures no duplicate artists are stored
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # count how many songs exist per genre
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # count how many songs exist per artist
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
