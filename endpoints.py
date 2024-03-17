import Person
import sim

from fastapi import FastAPI

app = FastAPI()

#create endpoint to start simulation. It receives the
#number of ICU beds and the number of common beds
@app.get("/start_simulation/{icu_beds}/{common_beds}")
async def start_simulation(icu_beds: int, common_beds: int):
    sim.start_simulation(icu_beds, common_beds)
    print(sim.simulat)
    return {"message": "Simulation started"}


@app.get("/day_statistics/{day}")
async def day_statistics(day:int):
    return sim.get_day_statistics(day)



