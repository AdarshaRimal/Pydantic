# Exporting pydantic model as python dict or json

from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'ktm', 'state': 'bagmati', 'pin': '4406'}

address1 = Address(**address_dict)

patient_dict = {'name': 'adarsha', 'age': 22, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)
temp2 = patient1.model_dump_json()

print(temp)
print(type(temp))
print(temp2)
print(type(temp2))