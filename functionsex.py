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


















