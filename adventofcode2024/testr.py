numbers = [100,5,10]
sum = 1050


def check_sum(number,numbers, sum):
    multiply = number*numbers[0]
    sumup = number+numbers[0]
    if multiply == sum: return True
    if sumup == sum: return True
    if len(numbers) == 1: return False
    if check_sum(multiply,numbers[1:len(numbers)],sum): return True
    if check_sum(sumup,numbers[1:len(numbers)],sum): return True
    return False

print (check_sum(numbers[0],numbers[1:len(numbers)],sum))