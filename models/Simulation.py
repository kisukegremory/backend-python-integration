from pydantic import BaseModel, Field
from typing import Literal

class SimulationResponse(BaseModel):
    amount: int = Field(ge=5000,le=150000, description='value of simulation', example=20000)
    duration: Literal[12, 18, 24, 36, 48] = Field(description='value of duration requested', example=24)
    cet_rate: float = Field(description='value of interest rate + taxes',example=0.03)

class Simulation(BaseModel):
    amount: int = Field(ge=5000,le=150000, description='value of simulation', example=20000)
    duration: Literal[12, 18, 24, 36, 48] = Field(description='value of duration requested', example=24)

    def simulate(self) -> SimulationResponse:
        return SimulationResponse(
            amount=self.amount*0.9,
            duration=self.duration,
            cet_rate=0.03
        )