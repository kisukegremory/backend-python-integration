from fastapi import FastAPI
import uvicorn
from models.Elegibility import Elegibility
from models.Simulation import Simulation, SimulationResponse
from models.Proposal import Proposal
from services import queues


app = FastAPI()

@app.post('/elegibility')
def post_elegility(elegibile: Elegibility):
    if elegibile.vehicle_debt:
        {'elegibility':False}
    x = queues.elegibility.send_message(MessageBody=elegibile.json())
    print(x)
    return {'elegibility':True}


@app.post('/simulation')
def post_simulation(simulation: Simulation) -> SimulationResponse:
    return simulation.simulate()


@app.post('/proposal')
def post_proposal(proposal: Proposal):
    return {'elegibility':'Success','proposal':proposal.json()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)