# Fórmulas
'''
f(n) = f(n - 1) + f(n - 2)
'''

def fibonnaci(num):
    if num in {0, 1}:
        return num
    return fibonnaci(num - 1) + fibonnaci(num - 2)

print([fibonnaci(i) for i in range(15)])