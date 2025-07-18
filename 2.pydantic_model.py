from pydantic import BaseModel
from typing import List,Dict,Optional
# step 1 : defining pydantic model
class Patient(BaseModel):
    name : str
    age : int
    weight : float
    married : bool = False
    tests : Optional[List[str]] = None #List instead of list for double type validation all values in the list should be string
    contact : Dict[str,str] #both key and value in the dict should be string

# defining insert function
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.tests)
    print('inserted into database')

# step 2 : creating object (instatiton of model)
patient_info = {'name':'Adarsha','age':22,'weight':50.5,'married':False,'tests' :['blood','urine'],'contact':{'email':'adarsha@gmail.com','phone':'9866754320'}}
# pydantic is smart enough for age = '22'
patient1 = Patient(**patient_info) #unpacking dictionary using **

# step 3 : passing the validated model object
insert_patient_data(patient1)