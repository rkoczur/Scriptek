import csv

def is_safe(row):
    row = [int(item) for item in row]
    row_check_dec = row.copy()
    row_check_inc = row.copy()
    row_check_dec.sort(reverse=True)
    row_check_inc.sort()

    if row != row_check_dec and row != row_check_inc:
        return 0
    
    for i in range(len(row)):
        if i == 0: continue
        if abs(row[i]-row[i-1]) > 3 or abs(row[i]-row[i-1]) < 1: return 0

    return 1

def is_dapened_safe(row):
    for i in range(len(row)):
        removed = row.copy()
        removed.pop(i)
        if is_safe(removed): return 1
    return 0

result_without_dampener = int()
result_with_dampener = int()

with open('R:\\0-Források\\Scriptek\\adventofcode2024\\day2.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter=' ')
    for row in lines:
        result_without_dampener += is_safe(row)
        result_with_dampener += is_dapened_safe(row)

print(result_without_dampener)
print(result_with_dampener)