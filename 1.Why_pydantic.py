# fucntion to add data to the databse (printing here for simpicity)

def insert_data(name,age): #two parameters name and age
    print(name)            # here actual db implementation can be done
    print(age)             # printing just for simplicity
    print('inserted into db')

insert_data('Adarsha','twenty')
# here any value is valid , if anyone only call function without knowing its implemenation,
# he try to add which data value is supported here any as dynamic typing nature of python
# but we want structured data in our data, so age must be integer here

def insert_data_updated(name:str,age:int): #type hinting
    print(name)
    print(age)
    print('inserted into db')

insert_data_updated('Adarsha','twenty') #now we get hint for name:str and age : int
# although hint is given but if we provide str value intead of int to age no error

def insert_data_condition(name,age):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('inserted into db')

    else:
        raise TypeError

insert_data_condition('adarsha','twenty')
# tird method correctly implementing type validation but it is not scalable
# -----> to fix this and for type and data validation we need pydantic