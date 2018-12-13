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



























