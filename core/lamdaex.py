


print('''


lambda expressions


''')



print('''



lambda argument1, argument2,... argumentN : expression using arguments
lambda is an expression, not a statement
lambda’s body is a single expression, not a block of statements



''')




f = lambda a , b, c : a+b+c

print(f(1,2,3))


x = lambda a="fee", b="fie", c="foe": a + b + c


print(x('foo'))


def knights():
    title = 'sir'
    action = (lambda x : title+'  '+x)
    return  action



ti = knights()

print(ti('hello'))





print('''


lambdas can be used in lists

''')


L = [lambda x: x ** 2, # Inline function definition
 lambda x: x ** 3,
 lambda x: x ** 4] # A list of three callable functions


for f in L:
 print(f(2)) # Prints 4, 8, 16


print(L[0](3))


print('''


lamdas can also be nested


''')



def action(x):
    return (lambda y : x+y)



r = action(4)
print(r(4))






action  = (lambda  x : (lambda y: (x+y)))



act = action(10)
print(act(10))



print('''


mapping functions over iterables


''')




li  = [1,2,3,4]

def inc(x) : return x+10


print(list(map(inc,li)))



print('''


selecting items in iterators


''')




print(list(filter((lambda  x : x>0) , range(-5,5))))


print('''


counting items in iteables


''')



from functools import reduce

print(reduce((lambda x, y :x+y),range(1,5)))
print(reduce((lambda x, y :x*y),range(1,5)))



import operator, functools
print(functools.reduce(operator.add, [2, 4, 6]))
print(functools.reduce(operator.mul, [2, 4, 6]))





print('''


program to find largest number in array 


''')


x = [1,2,3]

print (x[0]) if x.sort(reverse=True) is  None else ''













