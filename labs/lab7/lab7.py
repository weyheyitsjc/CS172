from Room import *
from maze import Maze
import sys
my_rooms = []
my_rooms.append(Room("This room is the entrance."))
my_rooms.append(Room("This room has a table. Maybe a dinning room?"))
my_rooms.append(Room('This room is the bathroom. take a shower.'))
my_rooms.append(Room('This room is the basement. Take a nap.'))
my_rooms.append(Room('This room is the yard. Get back inside.'))
my_rooms.append(Room("This room is empty. Maybe a ghost lives here."))
my_rooms.append(Room("This room is Le's bedroom. Nothing to steal."))
my_rooms.append(Room("This room attic. Don't disturb the spiders"))
my_rooms.append(Room('This room is full of books. When will you meet Snorlax.'))
my_rooms.append(Room('This room has a closet. Must be the entrance to Narnia.'))
my_rooms.append(Room("This room is the exit. Good Job."))

#room 0 is south of room 1
my_rooms[0].setNorth(my_rooms[1])
my_rooms[1].setSouth(my_rooms[0])
#Room 2 is east of room 1
my_rooms[1].setEast(my_rooms[2])
my_rooms[2].setWest(my_rooms[1])
#Room 3 is East of Room 2
my_rooms[2].setSouth(my_rooms[3])
my_rooms[3].setNorth(my_rooms[2])
#Room 4 
my_rooms[3].setEast(my_rooms[4])
my_rooms[4].setWest(my_rooms[3])
#Room 4 
my_rooms[4].setSouth(my_rooms[5])
my_rooms[5].setNorth(my_rooms[4])
#Room 4 
my_rooms[5].setWest(my_rooms[6])
my_rooms[6].setEast(my_rooms[5])
#Room 4 
my_rooms[6].setWest(my_rooms[7])
my_rooms[7].setEast(my_rooms[6])
#Room 4 
my_rooms[7].setSouth(my_rooms[8])
my_rooms[8].setNorth(my_rooms[7])
#Room 4 
my_rooms[8].setWest(my_rooms[9])
my_rooms[9].setEast(my_rooms[8])

my_rooms[9].setSouth(my_rooms[10])
my_rooms[10].setNorth(my_rooms[9])

if __name__ == '__main__':
    my_maze = Maze(my_rooms[0],my_rooms[10])
    while True:
        pos = my_maze.getCurrent()
        print(pos)
        my_maze.atExit()
        dir = input('Enter direction to move north west east south restart\n').lower()
        if dir == 'north':
            my_maze.moveNorth()
        elif dir == 'south':
            my_maze.moveSouth()
        elif dir == 'east':
            my_maze.moveEast()
        elif dir == 'west':
            my_maze.moveWest()
        elif dir == 'restart':
            my_maze.reset()
        else:
            print('Invalid Input')
    
        