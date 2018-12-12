


print('''


if else statements


''')


x =  'killer rabbit'

if x == 'roger' :
    print('hi roger')
elif x == 'snail' :
    print('hi snail')
else:
    print('run away ! run away !')



print('''


using backslashes for continuation

''')



a  = b =  1
c  = d =  2

if a == b and \
    c == d :
    print('''
    
    all are equal
    
    ''')


print('''


using braces


''')



if (a == b and
        c == d):
    print('''

    all are equal

    ''')


print('''


while loop
and break

''')


a = 10

while a > 0 :
    print(a)
    a -= 1
    if(a == 5):
        break

else :
    print('''
    
    a value completed
    
    ''')

print('''


while loop
and continue

''')

a = 10

while a > 0:
    a -= 1
    if (a == 5): continue
    print(a)


else:
    print('''

    a value completed

    ''')


'''
a = 10
while a == 10 : pass
else: print("not 10")

'''



print('''


for loops


''')



for x in range(4) :
    print(x)



s = 'humpback whales'

for x in s :
    print(x ,end ='\n')





t = [(1,2),(2,3),(3,4)]
for (x,y) in t :
    print(x,y)








