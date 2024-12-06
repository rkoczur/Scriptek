#Read csv to separate lists
import csv

list1 = list()
list2 = list()

with open('R:\\0-Források\\Scriptek\\adventofcode2024\\day1_1.csv') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        list1.append(int(row[0]))
        list2.append(int(row[1]))

list1.sort()
list2.sort()

result=int()

#Get distance
for i in range(len(list1)):
    result+=abs(list1[i]-list2[i])

print(result)

result = 0

#Get similarity
for element in list1:
    result += list2.count(element)*element

print(result)    