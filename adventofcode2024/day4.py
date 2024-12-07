input_data = open('adventofcode2024/day4.csv', 'r')
lines = input_data.readlines()

print(lines)
the_array = list()

for line in lines:
    line_chars = list(line)
    the_array.append(line_chars)

#CHECK HORIZONTAL
for row in the_array:
    
