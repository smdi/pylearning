


li = [1,2,3,4]

print(li)

print(len(li))

#add

li .append("hello")

print(li)

#delete

li.pop()

print(li)


li.pop(0)

print(li)

#sort

li.sort()

print(li)

#reverse


li.reverse()

print(li)


#nesting


print('''

nesting

''')

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

#get row 2
print(m[1])

print('''

get particular element 

''')


print(m[1][2])



print('''

usinig range functions

''')


print(list(range(4)))
print(list(range(-6,6,2)))


print('''

comprehensions and range

''')



print([[x*2,x*3] for x in range(4)] )


print('''


replacement or insertion


''')



l = [1,2,3,4]


l[1:2] = [7,8]


print(l)


print(l.sort())


print(l)



l = [1,2,3,4]

print(l.append(7))

print(l)







