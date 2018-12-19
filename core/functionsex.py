import time

print('''


def for functions


''')


def intersect(s1 , s2) :
    start = time.time()
    s = []
    for x in s1 :
        if x in s2:
            s.append(x)
    end = time.time()
    print('time taken by normal functuon is ' ,end-start)
    return  s



s1  = range(100000)

s2  = range(100000)

s = intersect(s1,s2)

#print(s)




print('''


same example usinig comprehensions


''')



def compint(s1,s2):
    start = time.time()
    s = []
    [s.append(x) for x in s1 if x in s2 ]
    end= time.time()
    print('time taken by comprehension functuon is ', end - start)
    return s


s1  = range(100000)

s2  = range(100000)

s = compint(s1,s2)

#print(s)




print('''


dir for printing all the attributes functions of object


''')


import math
import builtins
print(dir(builtins))
print(dir(math))



print('''




scopes



''')



x = 99

def fun():
    global  x
    x = 100


fun()
print(x)


print('''



scopes



''')




X = 99
def func1():
 global X
 X = 88
def func2():
 global X
 X = 77


print(X)
func1()
print(X)
func2()
print(X)




print('''


test for multiples 


''')



def almul(ch,rang):
    lst , r ,c = [] ,1 ,0
    for x in rang :
        r = x
        for y in range(ch):
            if  ch == c : break
            r *= x
            c += 1
        lst.append(r)
        c=1
    r=1
    return lst




print('''


squares


''')
sq = almul(2,range(5))
print(sq)


print('''


cubes


''')

cu  = almul(3,range(5))
print(cu)





print('''


avoiding mutable arguments changes


''')




print('without trick')

def changer(l):
    l[0] = 'spam'


l = [1,2,3,4]
print(l)
changer(l)
print(l)



print('applying trick')

s = [1,2,3,4]
print(s)
changer(s[:])
print(s)





print('''


return can send multiple values in form of tuple


''')



def multiple(x,y):
    x = 3
    y = [3,4]
    return x,y


x = 1
L = [ 1, 2]
x,L = multiple(x,L)

print(x,L)




print('''


working with functions


''')



def f(a, b = 4, c = 5): print('a = ',a,' b = ', b,'c = ', c)





f(1,2,3)
f(1,c=3,b=2)    #passig by keywords
f(1)            #default values to arguments





def func(spam, eggs, toast=0, ham=0):           # First 2 required
 print((spam, eggs, toast, ham))





func(1, 2)                                      # Output: (1, 2, 0, 0)
func(1, ham=1, eggs=0)                          # Output: (1, 0, 0, 1)
func(spam=1, eggs=0)                            # Output: (1, 0, 0, 0)
func(toast=1, eggs=2, spam=3)                   # Output: (3, 2, 1, 0)
func(1, 2, 3, 4)                                # Output: (1, 2, 3, 4)
func(1,2,toast=1,ham=1)





print('''


arbitary arguments


''')


print(''' * collects unmatched arguments into a tulpe  ''')



def f(*args):print(args)


f(1,2)
f(1,2,3,4,45,6,7,7,8,8,8,99,9,9,)
f(1,2,3,4,5,6)


print(''' 

    ** feature is similar 
 
    ** form allows you to convert from keywords to dictionaries,
 
 ''')


def df(**args) : print(args)



df(a= 1,b=2)
df(a = 1,b=2, c =3)



print('''


combinations of normal ,  *  and  **


''')


def comb(a, *pargs, **kargs): print(a, pargs, kargs)


comb(1 ,2,3 ,c=1,d=5 )




print('''




     for instance, how to decompose a task into purposeful functions (known as cohesion)
     how your functions should communicate (called coupling),



''')




print('''


summation using recursion


''')



def sumre(l):
    if not l :
        return 0
    else:
        return l[0] + sumre(l[1:])




sr = sumre([1,2,3,4])

print(sr)


print('''


printing a traingle


''')


def sumre(l):
    print(l)
    if not l :
        return 0
    else:
        return l[0] + sumre(l[1:])





sr = sumre([1,2,3,4,5])
print(sr)


print('''


alterate


''')


def mysum(L):
 return 0 if not L else L[0] + mysum(L[1:])



sr = mysum([1,2,3,4,5])

print(sr)



print('''


summation for arbitary arguments 


''')


def sumtree(l):
    tot = 0
    for x in l:
        if not isinstance(x , list):
            tot += x
        else :
            tot += sumtree(x)
    return tot



print(sumtree([1, [2, [3, [4, [5]]]]]))
print(sumtree([[[[[1], 2], 3], 4], 5]))






