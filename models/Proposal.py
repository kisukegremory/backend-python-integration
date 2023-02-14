from pydantic import BaseModel, Field
from typing import Literal


class Customer(BaseModel):
    cpf: str
    name: str
    email: str

class Residence(BaseModel):
    city: str
    state: Literal['SP','RJ','MG','OTHERS']
    zipcode: str = Field(title='cep',example='03021-000')

class Finance(BaseModel):
    income: float = Field(title='income monthly amount', example=1000, gt=0)
    source: Literal['CLT','UNEMPLOYED','BUSINESS','SELF SERVICE']


class Proposal(BaseModel):
    customer: Customer
    residence: Residence
    finance: Finance