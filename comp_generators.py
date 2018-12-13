


print('''


list comprehensions


''')




res = [ ord(x) for x in 'imran']


print(res)



print('''


map and lambda


''')




li  = list(map((lambda  x  : x**2),range(10)))

print(li)


print('''


finding even numpbers and odd numbers


''')



print('''

even numbers

''')

list(map((lambda x : print(x) if (x%2 == 0) else ' ' ) ,range(10) ))



print('''


odd numbers

''')


list(map((lambda x : print(x) if (x%2 != 0) else ' ' ) ,range(10) ))




print('''


squares of even numbers


''')




print(list(map((lambda  x : x**2),filter((lambda x :  x%2 == 0),range(10)))))


print('''


formal comprehension syntax


''')



print([

x + y for x in range(3)
      for y in range(3)
])



print('''


comprehensions and matrices


''')

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


for x in M :
    print(x)


print('''

getting a row

''')


print(M[1])


print('''


getting a column

''')


print([x[1] for x in M])



print([col+10 for row in M for col in row])



print('''


matrix muktipllication

''')


M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N=[[2, 2, 2], [3, 3, 3], [4, 4, 4]]




print( [M[row][col] * N[row][col] for row in range(3) for col in range(3)])







