
print('''


it is process of tracking runtime data of an application  or program

levels 
====================

debug()        =====      runs safely any time
info()         =====      represents that current function safely but u can cross check to verify 
                            whether is running safely or not
warning()      =====      current function will fail in future                          
error()        =====      current function has errors
critical()     =====      entire application may fail bcoz of errors in current function


''')



import logging

logging.basicConfig(filename= 'logging_folder/app.log' ,   level= logging.DEBUG)


def add(a,b):
    return a+b


def mul(a,b):
    return a*b


def div(a,b):
    return a%b


def sub(a,b):
    return a-b


def floor(a,b):
    return a//b




m = 10
n = 5


logging.debug('the addition of {} and {} is  {}'.format(m,n ,add(m,n)))
logging.info('the subtraction  of {} and {} is  {}'.format(m,n ,sub(m,n)))
logging.warning('the multiplication of {} and {} is  {}'.format(m,n ,mul(m,n)))
logging.error('the floor of {} and {} is  {}'.format(m,n ,floor(m,n)))
logging.critical('the division of {} and {} is  {}'.format(m,n ,div(m,n)))






