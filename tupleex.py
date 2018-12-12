


print('''

declaring a tuple 
tuple is immutable


''')


t  = (1,2,3,4)


print(t)
print('id' , id(t))


print('''

adding a value

''')



t =  t+(5,6)

print(t)

print('id' , id(t))


print('''

fetching a value

''')


print(t[0])



print('''

modifiying a vlaue does not work 


''')


print(
'''

we cannot remove a  element from tuple but we can make a new tuple
making a new tuple


'''
)



t  = (2,) + t[1:]

print(t)

print('id' , id(t))







