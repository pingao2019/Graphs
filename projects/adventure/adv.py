from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

 
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
# asc_room = ascii(room_graph)
# world.print_rooms(asc_room)

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []

def Traversal_direction(opposite_direct):
    if opposite_direct == 'e':
        return 'w'
    elif opposite_direct == 'w':
        return 'e'
    elif opposite_direct == 's':
        return 'n'
    elif opposite_direct == 'n':
        return 's'

 
stack= Stack()
visited = set()
 
while len(visited) < len(room_graph):

    path = []
     
    exit_direction = player.current_room.get_exits()

    visited.add(player.current_room)
   
     
    for newdirect in exit_direction:
        if player.current_room.get_room_in_direction(newdirect) not in visited:
            path.append(newdirect)
    
    
    if len(path) > 0:
        i = random.randint(0, len(path) - 1)
        stack.push(path[i])
        traversal_path.append(path[i])
        player.travel(path[i])
 
    else:
        stop = stack.pop()
        #room= Room()
        # traversal_path.append(room.connect_rooms(stop))
        # player.travel(room.connect_rooms(stop))
        traversal_path.append(Traversal_direction(stop))
        player.travel(Traversal_direction(stop))
        


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")