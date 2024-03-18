import sim

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# create endpoint to start simulation. It receives the
# number of ICU beds and the number of common beds


@app.get('/')
async def root():
    return {}

@app.get("/start_simulation")
async def start_simulation(icu_beds: int=10, common_beds: int=40):
    sim.start_simulation(icu_beds, common_beds)
    print(sim.simulat)
    return {"message": "Simulation started"}


@app.get("/day_statistics/{day}")
async def day_statistics(day:int):
    return sim.get_day_statistics(day)



