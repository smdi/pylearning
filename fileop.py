


print('''


opening a file and  writing to a file


''')



file = open('sample.txt','w')
text = 'hello im  hamza'
file.write(text)
file.close()






print('''



appending to a file


''')


file = open('sample.txt','a')
text = '\nwhats  is ur name ?\n my name is hamza'
file.write(text)
file.close()





print('''


open and reading a file


''')



file  = open('sample.txt','r')
text = file.readlines()
print(str(text))
file.close()

























