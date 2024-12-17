# -------------------------- #
#           CLASS            #
# -------------------------- #

class Equation:

    def __init__(self,result,nums):
        self.result = result
        self.nums = nums

    def get_result(self):
        return self.result
    
    def can_be_true(self):
        return self.check_sum(self.nums[0],self.nums[1:len(self.nums)])

    def check_sum(self,number,numbers):
        multiply = number*numbers[0]
        sumup = number+numbers[0]
        if multiply == self.result: return True
        if sumup == self.result: return True
        if len(numbers) == 1: return False
        if self.check_sum(multiply,numbers[1:len(numbers)]): return True
        if self.check_sum(sumup,numbers[1:len(numbers)]): return True
        return False  
    
# -------------------------- #
#           MAIN             #
# -------------------------- #

raw_equations = []   

input_data = open('adventofcode2024/day7.txt', 'r')
lines = input_data.readlines()
for line in lines:
    line = line.replace('\n','')
    eq_result = int(line.split(': ')[0])
    eq_nums = [int(s) for s in line.split(': ')[1].split(' ')]
    raw_equations.append([eq_result,eq_nums])
input_data.close()

counter = 0

for eq in raw_equations:
    this_equation = Equation(eq[0],eq[1])
    if this_equation.can_be_true(): counter+=this_equation.get_result()

print(counter)