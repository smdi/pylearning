import test_mod1


print('''


importing modules using from


''')


x = 'hello , im imran'

test_mod1.printer(x)




print('''


importing modules using from


''')




from test_mod1 import printer



printer(x)





print('''



third way of using modules --- from *


''')




from test_mod1 import *


printer(x)



test_mod1.x = 7


print(test_mod1.x)


test_mod1.y[0] = 'hello'

print(y)



from imp import reload
import test_mod1

test_mod1.tester()


