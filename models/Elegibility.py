from pydantic import BaseModel, Field


class Elegibility(BaseModel):
    cpf: str = Field(title='Cpf Documentation only numbers', max_length=11)
    vehicle_owner: bool = Field(title='Se a veículo está no nome da pessoa')
    vehicle_debt: bool = Field(title='Se o veículo tem alguma dívida e/ou não está quitado')
