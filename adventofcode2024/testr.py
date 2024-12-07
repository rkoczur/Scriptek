import re

def get_sumof_do_muls(row):
    summa = int()
    segment_one = row.split('do()')
    

#READ ALL LINES, AND SUM ALL OCCURENCES
input_data = open('adventofcode2024/day3.csv', 'r')
lines = input_data.readlines()
result = int()
summa = int()
for line in lines:
    segments = line.split('do()')
    for segment in segments:
        sub_segments = segment.split('don\'t()')
        pattern = r'mul\(\d+,\d+\)'
        muls = re.findall(pattern , sub_segments[0])
        for mul in muls:
            print(mul)
            cleaned=mul.replace('mul(','')
            cleaned=cleaned.replace(')','')
            nums = cleaned.split(',')
            summa += int(nums[0])*int(nums[1])
print (summa)