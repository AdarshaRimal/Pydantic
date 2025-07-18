from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import Optional,Annotated
class Student(BaseModel):
    name : str
    age : int
    email : EmailStr # for email validation
    linkedin : Optional[AnyUrl] = None # for url validation

def student_data(student : Student):
    print(student.name)
    print(student.age)
    print(student.email)
    print(student.linkedin)

student_info = {'name':'Adarsha','age':22,'email':'adarsharimal07@gmail.com','linkedin':'https://linkedin.com/1234'}

student1 = Student(**student_info)

student_data(student1)

# ----> Data Validation using Field
# class Student(BaseModel):
#     name : str = Field(max_length=50)
#     age : int = Field(gt = 0,lt = 100)
#     email : EmailStr
#     linkedin : Optional[AnyUrl] = None

# Filed can be used to add MetaData
class Student(BaseModel):
    name : Annotated[str,Field(max_length=50,title='Name of the student',description='Give the name of the student in less than 50 character',examples=['Adarsha','Ronaldo'])]

    age : Annotated[int,Field(gt=0,strict=True)] #using strict '22' --> error, provide 22 not '22'

    married : Annotated[bool,Field(default=False)] #default value using default parameter inside Field function
    email : EmailStr
    linkedin : Optional[AnyUrl] = None