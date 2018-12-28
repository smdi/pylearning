print(

'''

we can fetch the data from any database in python

each database has its own module like below

mysql        ---    pymysql
oracle       ---    cx_oracle
sql server   ---    pyodbc 


now we will configure mysql in python application  

when ever we specify db details in python application then automatically a connection will be created 
between database and python application 


python supports 

fetchone()      ->>>>> to get the first record 
fetchall()      ->>>>> to get all records 
fetchmany(n)    ->>>>> to get all records in tuple format

connect() is a default function in mysql module , 
takes four arguments 

host 
user 
password 
db 

it also supports cursor() to execute the connection between python and database 
here result displays tuple(all records ) and each record will be sub tuple

'''
)

import  pymysql
from  .config_file import *

connection  =  pymysql.Connect(host = host ,
                               user = user ,
                                password = password ,
                               db  = db
                                )


cursor  = connection.cursor()

sql =  'select * from  ' + tablename


cursor.execute(sql)

data = cursor.fetchall()


for i in data :
    print(i)

cursor.close()
connection.commit()
connection.close()

