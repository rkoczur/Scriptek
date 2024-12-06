#ADVENT OF CODE - DAY3

import csv
import re

#GET EVERY OCCURENCE OF NUMBERS INSIED MUL() AND RETURN THE SUM OF THEM
#USED CHATGPT FOR REGEXP - SHAME :(
def get_sumof_muls(row):
    summa = int()
    pattern = r'mul\(\d+,\d+\)'
    muls = re.findall(pattern , line)
    for mul in muls:
        cleaned=mul.replace('mul(','')
        cleaned=cleaned.replace(')','')
        nums = cleaned.split(',')
        summa += int(nums[0])*int(nums[1])
    return summa

#READ ALL LINES, AND SUM ALL OCCURENCES
input_data = open('adventofcode2024/day3.csv', 'r')
lines = input_data.readlines()
result = int()
for line in lines:
    result += get_sumof_muls(line)

print(result)