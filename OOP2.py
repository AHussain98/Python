class Song:
    """ class to represent a song """  # should always be triple quotes

    def __init__(self, title, artist, duration=None):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title  # this is a getter

    name = property(get_title)  # existing code will now work, as we have made name the same as the title
    # note we don't use parenthesis for the function
    # Python property() function returns the object of the property class and it is used to create property of a class.
    # Properties represent an intermediate functionality between a plain attribute (or field) and a method.
    # In other words, they allow you to create methods that behave like attributes.
    # With properties, you can change how you compute the target attribute whenever you need to do so.


# a_string = "this is a \n a string that has been split and \t tabbed"
# print(a_string)
# raw_string = r" the split \n and tabbing \t chars dont work in a raw string however"  # useful for regex or writing filepaths
# print(raw_string)
#
# help(Song)  #  help functions provide information on classes, including the docstrings
# Song.__init__.__doc__ = """ initialise the variables for the object"""   # we can add docstrings after declaration of the class
# # above is added docstring to the class's init function
#
# help(Song.__init__)

class Album:
    """ Class to represent a collection of songs"""
    def __init__(self, name, year, artist=None): # add a default value to the artist
        self.name = name
        self.year = year

        if artist is None:  # we can have logic branches in init method, artist here references the argument literal, not the member variable, hence no self
            self.artist = "Various"  # just a string, not an object
        else:
            self.artist = artist
        self.tracks = []  # create an empty list as a member variable

    def add_song(self, song, position=None):

        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(self, self.artist)

            if position is None:
                self.tracks.append(song_found)  # add it to the end of the list
            else:
                self.tracks.insert(position,song_found) # otherwise insert at the desired position

class Artist:
    """ a basic class to store artist details"""
    def __init__(self, name ):
        self.name = name
        self.albums = []  # empty list

    def add_album(self, album):
        if album not in self.albums:  # if it doesnt already exist in the list
            self.albums.append(album)
    # so currently the artist object will have a reference to the album objects
    # and the album objects will have a reference to an artist object
    # this can cause an issue with garbage collection, the runtime system removed memory for objects when they're no longer being referred to
    # as an example, if the program is no longer using the album associated with an artist, it cant reclaim the memory used by the album object
    # because it's still being referred to by the artists list of albums, this is circular referencing
    # we can avoid this by only storing strings of artists in the song class, and the name of the artist in the album class
    # then there is no need to store the objects themselves, since we can make use of the find_object() function

    def add_song(self, name, year, title):
        """ Add a new song to the collection of albums
        This method adds a song to an album in the collection
        The album should be created if it doesn't already exist"""
        album_found = find_object(name, self.albums)
        if album_found is None:  # if the album does not exist
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)
        album_found.add_song(title)  # implement into the album class's add_song method


def find_object(field, object_list):
    """
    check object list to see if an object with a 'name' attribute that matches exists, and returns it if it does
    """
    for object in object_list:
        if object.name == field:
            return object
    return None  # if it doesn't exist in the list


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt","r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field) # change this to an int
            print(artist_field,album_field,year_field,song_field)

            if new_artist is None:
                new_artist = Artist(artist_field)  # we have read up a new artist, so create an Artist object
                artist_list.append(new_artist)  #  add it to the list
            elif new_artist.name != artist_field: # or if the current new artist is not equal to the current artist field value
                # retrieve the artist object if there is one, if not then create a new object and add it to the artist list
                new_artist = find_object(artist_field,artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)  # append the object
                new_album = None

            if new_album is None:
               new_album = Album(album_field, year_field, new_artist)  # create a new album object now that we've created a new_artist object
               new_artist.add_album(new_album)  # add it at the point you create the object
            elif new_album.name != album_field:  # we've read a new album of the current artist
                # retrieve the album object if there is one
                # otherwise create a new album object and store it in the artists collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # now create a new songs object and add it to the current album collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list

def create_checkfile(artist_list):
    """ create a check file from object data for comparison with original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist,new_album,new_song), file=checkfile)

# at the moment, the current implementation of load_data has disadvantages, including needing to check the last line of the file every time
# and that fact that we dont check for existing artists objects when we encounter a new one
# we can change this so new objects are stored in their respective lists as soon as they're created

# the above approach uses classes but is not OOP, as we havent used inheritance, encapsulation, etc...

# remember that encapsulation involves encapsulating methods and data, not just methods

# lets rewrite load_data to delegate most of the work to the appropriate classes

def OOP_load_data():

    artist_list = []

    with open("albums.txt","r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field) # change this to an int
            print(artist_field,album_field,year_field,song_field)

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None: # we could not find the artist in the existing list
                new_artist = Artist(artist_field) # create the new object
                artist_list.append(new_artist)

            new_artist.add_song(album_field,year_field,song_field)

    return artist_list







if __name__ == '__main__':  # if the file is run as a script, then the following code executes
   artists = load_data()  # save the result
   print(len(artists))  # there are this many artists
   print(artists)

   create_checkfile(artists)
