
#DECLARATION AND READ RAW DATA INTO ARRAY
the_room = list()
current_pos_x = int()
current_pos_y = int()

#DIRECTIONS: U-up, L-left, R-right, D-down
current_direction = 'u'

input_data = open('adventofcode2024/day6.txt', 'r')
lines = input_data.readlines()
for line in lines:
    the_room.append(list(line.replace('\n','')))

#CHECK IS CURRENT POSITION IS INSIDE THE ROOM
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

while is_inside(current_pos_x,current_pos_y):
    