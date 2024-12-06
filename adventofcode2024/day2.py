import csv

result = int()

def is_safe(row):
    row = [int(item) for item in row]
    row_check_dec = row.copy()
    row_check_inc = row.copy()
    row_check_dec.sort(reverse=True)
    row_check_inc.sort()

    print(row)
    print(row_check_dec)
    print(row_check_inc)

    if row != row_check_dec and row != row_check_inc:
        return 0
    
    for i in range(len(row)):
        if i == 0: continue
        if abs(row[i]-row[i-1]) > 3 or abs(row[i]-row[i-1]) < 1: return 0

    return 1

with open('R:\\0-Források\\Scriptek\\adventofcode2024\\day2.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter=' ')
    for row in lines:
        result += is_safe(row)

print(result)