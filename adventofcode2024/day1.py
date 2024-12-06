# ADVENT OF CODE DAY 1
import csv

# READ SOURCE INTO SEPARATE LISTS AND SORT THEM ASCENDING
list1 = list()
list2 = list()

with open('R:\\0-Források\\Scriptek\\adventofcode2024\\day1.csv') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        list1.append(int(row[0]))
        list2.append(int(row[1]))

list1.sort()
list2.sort()

#GET DISTANCE AND PRINT TO CONSOLE

dist = int()

for i in range(len(list1)):
    dist+=abs(list1[i]-list2[i])

print(dist)

#GET SIMILARITY AND PRINT TO CONSOLE

sim = int()
for element in list1:
    sim += list2.count(element)*element

print(sim)    