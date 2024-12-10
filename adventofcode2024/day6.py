
# -------------------------- #
#         DECLARATION        #
# -------------------------- #

the_room = list()
current_pos_x = int()
current_pos_y = int()
counter = 0

#DIRECTIONS: 0-up, 1-right, 2-down, 3-left
current_direction = 0

input_data = open('adventofcode2024/day6.txt', 'r')
lines = input_data.readlines()
for line in lines:
    the_room.append(list(line.replace('\n','')))

# -------------------------- #
#         FUNCTIONS          #
# -------------------------- #

#RETURN THE NEXT PLACE COORDINATES ACCORDING TO DIRECTION
def get_next_place(current_pos_x,current_pos_y):
    next_place = [current_pos_x,current_pos_y]
    if current_direction == 0:
        next_place = [current_pos_x,current_pos_y-1]
    elif current_direction == 1:
        next_place = [current_pos_x+1,current_pos_y]
    elif current_direction == 2:
        next_place = [current_pos_x,current_pos_y+1]
    elif current_direction == 3:
        next_place = [current_pos_x-1,current_pos_y]
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

#GET STARTING POSITION
for y, row in enumerate(the_room):
    for x, pos in enumerate(row):
        if pos == '^': 
            current_pos_x = x
            current_pos_y = y

# -------------------------- #
#           MAIN             #
# -------------------------- #

while True:
    next_place = get_next_place(current_pos_x,current_pos_y)
    next_place_x = next_place[0]
    next_place_y = next_place[1]
    if not is_inside(next_place_x,next_place_y):
        the_room[current_pos_y][current_pos_x] = 'X'
        break
    if the_room[next_place_y][next_place_x] == '#':
        current_direction = change_direction(current_direction)
    else:
        the_room[current_pos_y][current_pos_x] = 'X'
        current_pos_x = next_place_x
        current_pos_y = next_place_y

for row in the_room:
    for col in row:
        if col == 'X': counter +=1

print(counter)