#LOAD RAW DATA
input_data = open('adventofcode2024/day4.csv', 'r')
lines = input_data.readlines()
counter = 0

#MAKE A TWO DIMENSION ARRAY
the_array = list()
for line in lines:
    line_chars = list(line)
    the_array.append(line_chars)

#CHECK EVERY DIRECTION OF THE WORDS IN THE ARRAY
#A little bit of 'brute force solution' - sorry I was tired :D

for row_index, row in enumerate(the_array):
    for col_index, col in enumerate(row):
            #HORIZONTAL
            if col_index + 3 < len(row):
                if row[col_index] == 'X' and row[col_index+1] == 'M' and row[col_index+2] == 'A' and row[col_index+3] == 'S':
                    counter +=1
            if col_index - 3 >= 0:
                if row[col_index] == 'X' and row[col_index-1] == 'M' and row[col_index-2] == 'A' and row[col_index-3] == 'S':
                    counter +=1
            #VERTICAL
            if row_index + 3 < len(the_array):
                if the_array[row_index][col_index] == 'X' and the_array[row_index+1][col_index] == 'M' and the_array[row_index+2][col_index] == 'A'and the_array[row_index+3][col_index] == 'S':
                    counter +=1
            if row_index - 3 >= 0:
                if the_array[row_index][col_index] == 'X' and the_array[row_index-1][col_index] == 'M' and the_array[row_index-2][col_index] == 'A'and the_array[row_index-3][col_index] == 'S':
                    counter +=1
            #DIAGONAL
            if col_index + 3 < len(row) and row_index + 3 < len(the_array):
                if  the_array[row_index][col_index] == 'X' and the_array[row_index+1][col_index+1] == 'M' and the_array[row_index+2][col_index+2] == 'A'and the_array[row_index+3][col_index+3] == 'S':
                    counter +=1
            if col_index - 3 >= 0 and row_index - 3 >= 0:
                if the_array[row_index][col_index] == 'X' and  the_array[row_index-1][col_index-1] == 'M' and the_array[row_index-2][col_index-2] == 'A'and the_array[row_index-3][col_index-3] == 'S':
                    counter +=1
            if col_index - 3 >= 0 and row_index + 3 < len(the_array):
                if the_array[row_index][col_index] == 'X' and the_array[row_index+1][col_index-1] == 'M' and the_array[row_index+2][col_index-2] == 'A'and the_array[row_index+3][col_index-3] == 'S':
                    counter +=1
            if col_index + 3 < len(row) and row_index - 3 >= 0:
                if the_array[row_index][col_index] == 'X' and  the_array[row_index-1][col_index+1] == 'M' and the_array[row_index-2][col_index+2] == 'A'and the_array[row_index-3][col_index+3] == 'S':
                    counter +=1

counter = 0

for row_index, row in enumerate(the_array):
    for col_index, col in enumerate(row):
        if col == 'A':
            c = 0
            if col_index + 1 < len(row) and row_index + 1 < len(the_array) and col_index - 1 >=0 and row_index -1 >=0:
                if the_array[row_index-1][col_index-1] == 'M' and the_array[row_index+1][col_index+1] == 'S':
                    c +=1
                if the_array[row_index-1][col_index+1] == 'M' and the_array[row_index+1][col_index-1] == 'S':
                    c +=1
                if the_array[row_index+1][col_index+1] == 'M' and the_array[row_index-1][col_index-1] == 'S':
                    c +=1
                if the_array[row_index+1][col_index-1] == 'M' and the_array[row_index-1][col_index+1] == 'S':
                    c +=1
            if c==2: counter += 1

print(counter)