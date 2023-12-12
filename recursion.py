#FÓRMULAS
'''
n! = n * (n - 1)!
'''

def factorial(num: int):
    result = 1
    if num == 1 or num == 0:
        return result
    else:
        return num * factorial(num - 1)


print(factorial(6))