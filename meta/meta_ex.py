


print('''
      
      
      custom meta classes
      

   ''')



class Meta(type):
    def __new__(cls, names , bases , dct):
        print('''                        
                     im meta classes                                          
              ''')
        x = super().__new__(cls , names , bases , dct)
        x.attr = 100
        return x
    # def __init__(self ):
    #     self.user = user





class A(metaclass= Meta) :
    pass

class B(metaclass=Meta):
        pass


class C(metaclass= Meta) :
    pass




x = A()
print(x.attr)
# print(x.user)

x = B()
print(x.attr)
# print(x.user)

x = C()
print(x.attr)
# print(x.user)










