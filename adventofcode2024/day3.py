#ADVENT OF CODE - DAY3

import csv
import re

#GET EVERY OCCURENCE OF NUMBERS INSIED MUL() AND RETURN THE SUM OF THEM
#USED CHATGPT FOR REGEXP - SHAME :(
def get_sumof_muls(line):
    summa = int()
    pattern = r'mul\(\d+,\d+\)'
    muls = re.findall(pattern , line)
    for mul in muls:
        cleaned=mul.replace('mul(','')
        cleaned=cleaned.replace(')','')
        nums = cleaned.split(',')
        summa += int(nums[0])*int(nums[1])
    return summa

def get_sumof_do_muls(line):
    summa = int()
    segments = line.split('do()')
    for segment in segments:
        sub_segments = segment.split('don\'t()')
        pattern = r'mul\(\d+,\d+\)'
        muls = re.findall(pattern , sub_segments[0])
        for mul in muls:
            cleaned=mul.replace('mul(','')
            cleaned=cleaned.replace(')','')
            nums = cleaned.split(',')
            summa += int(nums[0])*int(nums[1])
    return summa


#READ ALL LINES, AND SUM ALL OCCURENCES
input_data = open('adventofcode2024/day3.csv', 'r')
lines = input_data.readlines()
result_one = int()
result_two = int()
for line in lines:
    result_one += get_sumof_muls(line)

print(result_one)

#SUM ONLY OCCURENCES AFTER DO()
for line in lines:
    result_two += get_sumof_do_muls(line)

print (result_two)