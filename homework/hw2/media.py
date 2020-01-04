#File: media.py
#Purpose: Contains media classes used to run media program of homework 2
#Name: Jacy Yu
#Drexel ID: jy529
#Date: May 3, 2019

#parent class Media
class Media():
#initialize attributes for any media objects (type, name, rating)
    def __init__(self, mtype, mname, mrating):
        self.__mtype = mtype
        self.__mname = mname
        self.__mrating = mrating
    
#str overloaded to give info
    def __str__(self):
        media = ""
        media += "Type: " + self.__mtype + "\nName: " + self.__mname + "\nRating: " + self.__mrating
        return media
    
#getter method to the type of the media
    def getType(self):
        return self.__mtype
    
#getter method to get the name of the media
    def getName(self):
        return self.__mname

#movie class, inherited from Media parent class
class Movie(Media):
#initialize attributes for movie objects, inherits media attributes and creates attributes special to movie objects
    def __init__(self, mtype, mname, mrating, director, runningtime):
        super().__init__(mtype, mname, mrating)
        self.__director = director
        self.__runningtime = runningtime

#overridden __str__ in parent class, inherited parent str and adds new movie info.
    def __str__(self):
        movie = super().__str__()
        movie += "\nDirector: " + self.__director + "\nRunning Time: " + self.__runningtime
        return movie
    
#play method to print play string if user decides to play a movie
    def play(self):
        moviePlay = ""
        moviePlay += self.getName() + ", playing now"
        print(moviePlay)
        
#index the object to retreive the type "movie" and the name
    def __getitem__(self, key):
        if key == 0:
            return "movie"
        elif key == 1:
            return self.getName()
    
#Song class, inherited from Media parent class
class Song(Media):
#initialize attributes for song objects, inherits media attributes and creates attributes special to song objects
    def __init__(self, mtype, mname, mrating, artist, album):
        super().__init__(mtype, mname, mrating)
        self.__artist = artist
        self.__album = album
        
#overridden __str__ in parent class, inherited parent str and adds new song info.
    def __str__(self):
        song = super().__str__()
        song += "\nArtist: " + self.__artist + "\nAlbum: " + self.__album
        return song
        
#play method to print play string if user decides to play a song
    def play(self):
        songPlay = ""
        songPlay += self.getName() + " by " + self.__artist + ", playing now"
        print(songPlay)
        
#index the object to retreive the type "song" and the name
    def __getitem__(self, key):
        if key == 0:
            return "song"
        elif key == 1:
            return self.getName()
    
#Picture class, inherited from Media parent class
class Picture(Media):
#initialize attributes for picture objects, inherits media attributes and creates attributes special to picture objects
    def __init__(self, mtype, mname, mrating, resolution = "200 dpi"):
        super().__init__(mtype, mname, mrating)
        self.__resolution = resolution
    
#overridden __str__ in parent class, inherited parent str and adds new picture info.
    def __str__(self):
        picture = super().__str__()
        picture += "\nResolution: " + self.__resolution
        return picture
    
#show method to print show string if user decides to display a picture
    def show(self):
        showPic = ""
        showPic += "Showing " + super().getName()
        print(showPic)

#index the object to retreive the type "picture" and the name
    def __getitem__(self, key):
        if key == 0:
            return "picture"
        elif key == 1:
            return self.getName()
        