


s1  = set([1,2,3,4,5,6,6])

print(s1)

print('''

set does not allow duplicates

''')



print('''


adding a value


''')



s1.add(8)


print(s1)


print('''


adding multiple values


''')


s1.update([12,35,89,99])



print(s1)




print('''


deleting a value


''')


s1.remove(1)

print(s1)

s1 = set([1,2,3])
s2 = set([3,4,5])


print('''

intesection of sets

''')


s3  = s1.intersection(s2)

print(s3)


print('''

difference of sets

''')


s3  = s1.difference(s2)

print(s3)


s3  = s1.symmetric_difference(s2)

print(s3)





print('''

union of sets

''')


s3  = s1.union(s2)

print(s3)



















