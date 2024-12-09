
#DECLARATION AND LOAD RAW DATA
rules = list()
updates = list()
counter_valid = 0
counter_corrected = 0
input_data = open('adventofcode2024/day5.txt', 'r')
lines = input_data.readlines()

#GET RULES AND UPDATES INTO STRUCTURED DATASETS
for line in lines:
    line_cleaned = line.replace('\n','')
    if '|' in line:
        splitted = line_cleaned.split('|')
        integer_list = [int(s) for s in splitted]
        rules.append(integer_list)
    else:
        if not ',' in line:
            continue
        pages = line_cleaned.split(',')
        integer_list = [int(s) for s in pages]
        updates.append(integer_list)

#RETURN TRUE IF TWO NUMBERS ARE IN THE RIGHT ORDER
def check_rules(num1,num2):
    for rule in rules:
          if rule[0]==num1 and rule[1] == num2:
               return True
    return False

#RETURN THE MIDDLE INDEX OF A LIST
def middle(update):
    return update[int(len(update)/2)]

#RETURN TRUE IF ALL NUMBERS ARE IN THE CORRECT POSITION
def valid(update):
    is_valid = True
    for i,num in enumerate(update):
         for j in range(i+1,len(update)):
              if check_rules(update[i], update[j]):
                   is_valid = True
              else:
                   return False
    return True

#SWAP THE NUMBERS WHICH ARE IN INCORRECT POSITIONS
def correct_update(update):
     for i,num in enumerate(update):
         for j in range(i+1,len(update)):
              if not check_rules(update[i], update[j]):
                   update[i], update[j] = update[j], update[i]
     return update

#CHECK IF UPDATE IS VALID AND GET SUM CENTER VALUES
for update in updates:
        if valid(update):
            print(update)
            counter_valid += middle(update)
        else:
            counter_corrected += middle(correct_update(update))

print(counter_valid)
print(counter_corrected)