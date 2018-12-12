
'''

declaring a dictionary

'''

d = {}


print('''

adding an item

''')

d['eid'] = 101
d['esal'] = 10000
d['ename'] = 'chinti'

#or

d.update({'eloc':'hyd'})



print(d)


#modifiying value

d['eid'] = 102

#deleting a value




print('''


using pop item

''')


print(d.popitem())
print(d)



print('''

using a pop 

''')


d.pop('eid')

print(d)


print('''


fetching a value using get


''')

print(d.get('esal'))



print('''

using nesting

''')



m = {

    'name' : {'first':'shaik','last':'imran'} ,
    'location':['pune', 'hyderabad'] ,
    'age' : 18
}



print('''


fetcing a value 

''')


print(m['name']['last'])
print(m['name']['first'])


print('''


appending a value 


''')


m['location'].append('shimla')
#m['town'].append('tirupati')

print(m)



