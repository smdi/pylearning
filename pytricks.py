

print('''


pytrick1


''')

x = ( 1+
      2+
      3+
      4 )

print(x)



print('''


pytrick2


''')


a = 2
b = 4
c = 3

if (

    a == 2
     and
    b == 4
     and
    c == 3
   ):

    print('all are equal')



print('''


pytrick3


''')


if a == 2 : print('hello')



print('''


pytrick4


''')


while True :
    ip  = input('''
    
       enter a string to reply
    
    ''')

    if ip == 'stop' : break

    print("""
    
    
    
    \t
    
    
    
    """ + ip.upper())



print('''


assigning a list of values to list of names


''')

[a,b,c] = (1,2,3)




print(a , b , c)


print('''



sequence unpacking



''')


seq = (1,2,3,4)

a , b , c , d = seq


print(a,b,c,d)


print('''


multiple target assignment


''')


a= b= c = d  = 8

print(a,b,c,d)




print('''



appending a value to list 


''')


print('''

wrong way 

''')


l =[1,2,3,4]

l = l.append(5) #---------------> SHOULD NOT DO THIS

print(l)


print('''

correct way

''')


L = [1,2,3,4]

L.append(5)

print(L)



