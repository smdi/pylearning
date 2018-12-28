



def smart_div(function):
    def inner(a,b) :
        print('Im gonna divide now')
        if b == 0 :
            print('cannot divide')
            return
        return function(a,b)
    return inner



@smart_div
def div(a,b):
    return print(a/b)


div(2,5)
div(2,0)



















