
# -------------------------- #
#         DECLARATION        #
# -------------------------- #

the_room = list()
current_pos = [int(),int()]
places_of_guard = list()
counter = 0
starting_pos = list()

#DIRECTIONS: 0-up, 1-right, 2-down, 3-left
current_direction = 0

input_data = open('adventofcode2024/day6.txt', 'r')
lines = input_data.readlines()
for line in lines:
    the_room.append(list(line.replace('\n','')))
input_data.close()

# -------------------------- #
#         FUNCTIONS          #
# -------------------------- #

#RETURN THE NEXT PLACE COORDINATES ACCORDING TO DIRECTION
def get_next_place(current_pos):
    next_place = [current_pos[0],current_pos[1]]
    if current_direction == 0:
        next_place[1] = next_place[1]-1
    elif current_direction == 1:
        next_place[0] = next_place[0]+1
    elif current_direction == 2:
        next_place[1] = next_place[1]+1
    elif current_direction == 3:
        next_place[0] = next_place[0]-1
    return next_place

#CHANGE THE CURRENT DIRECTION
def change_direction(current_direction):
    if current_direction<3:
        current_direction += 1
    else: 
        current_direction = 0
    return current_direction

#CHECK IF CURRENT POSITION IS INSIDE THE ROOM
def is_inside(x,y):
    if x >= len(the_room[0]): return False
    if x < 0: return False
    if y >= len(the_room): return False
    if y < 0: return False
    return True

def in_move_list(move_list):
    for move in move_list:
            if move[0] == current_pos[0] and move[1] == current_pos[1] and move[2] == current_direction:
                return True
    return False

def move_string(x,y,direction):
    return str(x)+','+str(y)+','+str(direction)

def pos_string(x,y):
    return str(x)+','+str(y)

# -------------------------- #
#           MAIN             #
# -------------------------- #

#GET STARTING POSITION
for y, row in enumerate(the_room):
    for x, pos in enumerate(row):
        if pos == '^': 
            current_pos[0]=x
            current_pos[1]=y
            starting_pos = current_pos.copy()

#DO THE WALK
while True:
    next_place = get_next_place(current_pos)
    if not is_inside(next_place[0],next_place[1]):
        if current_pos not in places_of_guard: places_of_guard.append(current_pos.copy())
        break
    if the_room[next_place[1]][next_place[0]] == '#':
        current_direction = change_direction(current_direction)
    else:
        if current_pos not in places_of_guard: places_of_guard.append(current_pos.copy())
        current_pos[0] = next_place[0]
        current_pos[1] = next_place[1]

print(len(places_of_guard))

#TRY LOOPING
loop_positions = []
map_to_check = []

for index, place in enumerate(places_of_guard):
    print(place)
    if index==0:continue
    current_direction = 0
    current_pos = starting_pos.copy()
    move_list = set()
    map_to_check = []
    for line in lines:
        map_to_check.append(list(line.replace('\n','')))
    map_to_check[place[1]][place[0]] = '#'
    new_places_of_guard = set()

    while True:
        next_place = get_next_place(current_pos)
        if move_string(next_place[0],next_place[1],current_direction) in move_list:
            if place not in loop_positions: loop_positions.append(place.copy())
            break
        if not is_inside(next_place[0],next_place[1]):
            if pos_string(current_pos[0],current_pos[1]) not in new_places_of_guard: new_places_of_guard.add(pos_string(current_pos[0],current_pos[1]))
            break
        if map_to_check[next_place[1]][next_place[0]] == '#':
            current_direction = change_direction(current_direction)
        else:
            if pos_string(current_pos[0],current_pos[1]) not in new_places_of_guard: new_places_of_guard.add(pos_string(current_pos[0],current_pos[1]))
            current_pos[0] = next_place[0]
            current_pos[1] = next_place[1]
            move_list.add(move_string(current_pos[0],current_pos[1],current_direction))
        

print(len(loop_positions))