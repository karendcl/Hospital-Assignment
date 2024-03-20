import { Link } from "react-router-dom"
import { BASEURL } from "../Utils/urlUtils"

function HomePage() {

  const handleClickSim= ()=>{
    const startSim = async ()=>{
      const response = await fetch(`${BASEURL}/start_simulation`)
      const data = await response.json()
    }

    startSim()
  }

  return (
    <>
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className=" text-5xl pb-10">HOME PAGE</h1>
      <Link className= "bg-blue-600 h-20 w-32 text-lg font-bold rounded-lg flex flex-col justify-center items-center" onClick={handleClickSim} to="/results/0">
        <p>Start</p> <p>Simulation</p>
      </Link>
    </div>
    </>
  )
}

export default HomePage
