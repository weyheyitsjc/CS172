#File: main.py
#Purpose: Main file (program) of homework 2
#Name: Jacy Yu
#Drexel ID: jy529
#Date: May 3, 2019

from media import *

#list of medias
mediaLibrary = [ 
    Movie("Movie", "Us", "7.4/10", "Jordan Peele", "1h 56min"),
    Movie("Movie", "Shazam!", "7.6/10", "David F. Sandberg", "2h 12min"),
    Movie("Movie", "Dumbo", "6.6/10", "Tim Burton", "1h 52min"),
    Movie("Movie", "Five Feet Apart", "7.1/10", "Justin Baldino", "1h 56min"),
    Movie("Movie", "Avengers: Endgame", "9.1/10", "Anthony Russo, Joe Russo", "3h 1min"),
    Song("Song", "Good News", "5/5", "Ocean Park Standoff", "Ocean Park Standoff - EP"),
    Song("Song", "Boy With Luv", "5/5", "BTS", "MAP OF THE SOUL: PERSONA"),
    Song("Song", "Yellow", "4.7/5", "Coldplay", "Parachutes"),
    Song("Song", "Sunflower", "4.4/5", "Post Malone and Swae Lee", "Spider-Man: Into the Spider-Verse Soundtrack"),
    Picture("Picture", "Mona Lisa.jpg", "10/10"),
    Picture("Picture", "The Starry Night.jpg", "8/10", "300 dpi"),
    Picture("Picture", "Girl with a Pearl Earring.jpg", "6.7/10", "600 dpi"),
    Picture("Picture", "American Gothic.jpg", "7.4/10", "450 dpi")
    ]

songs = []
movies = []
pictures = []
playableMedia = []

#sort all medias into their categories
for media in mediaLibrary: 
    if media[0] == "song":
        songs.append(media)
        playableMedia.append(media)
    elif media[0] == "movie":
        movies.append(media)
        playableMedia.append(media)
    elif media[0] == "picture":
        pictures.append(media)
        
#display menu
def menu():
    print("Menu: (type to get command)")
    print("'quit' or 'exit' to exit the program\n")
    print("'display all' for all media in the library")
    print("'display songs' for all songs in the library")
    print("'display movies' for all movies in the library")
    print("'display pictures' for all pictures in the library\n")
    print("'play <<song name>>' to play a song")
    print("'play <<movie title>>' to play a movie")
    print("'display <<picture name.extension>>' to display a picture")

#display all medias in list
def displayAll():
    for media in mediaLibrary:
        print(media, "\n")
    
#display the different types of medias, e.g. songs, movies, pictures
def displayMedia(userMedia, mediaList):
    if userMedia == "display songs":
        print("All songs in the library below:")
        print("(All information courtesy of Amazon music)")
        for song in mediaList:
            print(song, "\n")
    elif userMedia == "display movies":
        print("All movies in the library below:")
        print("(All information courtesy of IMDb)")
        for movie in mediaList:
            print(movie, "\n")
    elif userMedia == "display pictures":
        print("All pictures in the library below:")
        for picture in mediaList:
            print(picture, "\n")
            
#function to play certain song or movie
def playMedia(playableMedia, mediasList): 
    played = 0
    playableMedia = playableMedia.replace("play", "")
    playableMedia = playableMedia.replace(" ", "", 1)
    medias = playableMedia
    playableMedia = playableMedia.lower()
    for media in mediasList:
        if playableMedia == media[1].lower():
            played += 1
        else:
            continue
    if played == 1:
        for media in mediasList:
            if playableMedia == media[1].lower():
                return media.play()
            else:
                continue
    elif played == 0:
        print("'" + medias + "'" + " not in library")

#function to display certain pictures
def displayPicture(picture, pictureList):
    matched = 0
    picture = picture.replace("display", "")
    picture = picture.replace(" ","", 1)
    media = picture
    picture = picture.lower()
    for image in pictureList:
        if picture == image[1].lower():
            matched += 1
        else:
            continue
    if matched == 1:
        for image in pictureList:
            if picture == image[1].lower():
                return image.show()
            else:
                continue
    elif matched == 0:
        print("'" + media + "'" + "not in library")

print("Welcome to media player!\n")
menu()

command = input("What do you want to do?\n")
running = True

#checking user input for what they want program to do 
while running: 
    if command.lower() == "display all":
        displayAll()
        print("Type 'quit' or 'exit' to exit program")
        print("Type 'menu' to show menu commands again")
        command = input("What do you want to do?\n")
    elif command.lower() == ("display songs"):
        media = command.lower()
        displayMedia(media, songs)
        print("Type 'quit' or 'exit' to exit program")
        print("Type 'menu' to show menu commands again")
        command = input("What do you want to do?\n")
    elif command.lower() == ("display movies"):
        media = command.lower()
        displayMedia(media, movies)
        print("Type 'quit' or 'exit' to exit program")
        print("Type 'menu' to show menu commands again")
        command = input("What do you want to do?\n")
    elif command.lower() == ("display pictures"):
        media = command.lower()
        displayMedia(media, pictures)
        print("Type 'quit' or 'exit' to exit program")
        print("Type 'menu' to show menu commands again")
        command = input("What do you want to do?\n")
    elif ("dis") in command.lower():
        displayPicture(command, pictures)
        print()
        print("\nType 'quit' or 'exit' to exit program")
        print("Type 'menu' to show menu commands again")
        command = input("What do you want to do?\n")
    elif ("play") in command.lower():
        playMedia(command, playableMedia)
        print("\nType 'quit' or 'exit' to exit program")
        print("Type 'menu' to show menu commands again")
        command = input("What do you want to do?\n")
    elif command.lower() == "menu":
        menu()
        command = input("What do you want to do?\n")
    elif command.lower() == ("quit"):
        running = False
    elif command.lower() == ("exit"):
        running = False
    else:
        print("Command not valid.")
        print("Please try again.")
        print("Type 'menu' to show menu commands again")
        command = input("What do you want to do?\n")
        
print("Thank you. Goodbye.")