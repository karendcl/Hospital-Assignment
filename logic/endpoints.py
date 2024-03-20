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
async def start_simulation(icu_beds: int = 10, common_beds: int = 40):
    sim.start_simulation(icu_beds, common_beds)
    return {"message": "Simulation started"}


@app.get("/day_statistics/{day}")
async def day_statistics(day: int):
    return sim.get_day_statistics(day)


@app.get("/stats/cured")
async def cured():
    return sim.get_cured()


@app.get("/stats/deaths")
async def deaths():
    return sim.get_deaths()


@app.get("/stats/better")
async def better():
    return sim.get_patients_better()


@app.get("/stats/worse")
async def worse():
    return sim.get_patients_worse()

@app.get("/stats/critical")
async def critical():
    return sim.get_critical_rundown()

@app.get("/stats/grave")
async def grave():
    return sim.get_grave_rundown()

@app.get("/stats/regular")
async def regular():
    return sim.get_regular_rundown()








