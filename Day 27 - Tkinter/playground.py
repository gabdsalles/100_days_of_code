def add(*args):
    soma = 0
    for number in args:
        soma += number
    
    print(soma)

add(1, 2, 3, 5, 99)
add(123, 669)

#Default values - function
def foo (a, b=4, c= 6):
    print(a,b,c)

foo(1, 7)
foo(20, b=5)