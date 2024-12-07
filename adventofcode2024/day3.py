#ADVENT OF CODE - DAY3

import csv
import re

# GET THE "MUL(N,N)" OCCURENCES AND RETURN WITH A LIST OF THEM
def find_muls(source_string):
    pattern = r'mul\(\d+,\d+\)'
    return re.findall(pattern , source_string)

# CLEAN EVERTHING EXCEPT THE TWO NUMBERS AND RETURN WITH A LIST OF THEM
def clean_mul_and_sum(mul):
    cleaned=mul.replace('mul(','')
    cleaned=cleaned.replace(')','')
    return cleaned.split(',')

# GET ALL NUMBER PAIRS OF THE LINE AND RETURN THE SUM OF THEM
def get_sumof_muls(line):
    summa = int()
    muls = find_muls(line)
    for mul in muls:
        nums = clean_mul_and_sum(mul)
        summa += int(nums[0])*int(nums[1])
    return summa

# GET ALL NUMBER PAIRS BETWEEN do() AND don't() AND RETURN THE SUM OF THEM
def get_sumof_do_muls(line):
    summa = int()
    segments = line.split('do()')
    for segment in segments:
        sub_segments = segment.split('don\'t()')
        muls = find_muls(sub_segments[0])
        for mul in muls:
            nums = clean_mul_and_sum(mul)
            summa += int(nums[0])*int(nums[1])
    return summa


# READ ALL LINES, AND SUM ALL OCCURENCES
input_data = open('day3.csv', 'r')
lines = input_data.readlines()
result_one = int()
result_two = int()
for line in lines:
    result_one += get_sumof_muls(line)

print(result_one)

# SUM ONLY OCCURENCES AFTER DO()
concatenated = str()
for line in lines:
    concatenated = concatenated + line
result_two += get_sumof_do_muls(concatenated)

print (result_two)