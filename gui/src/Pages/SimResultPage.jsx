import { useEffect, useState } from "react"
import { Link, useParams } from "react-router-dom"
import ShowData from "./Components/ShowData"
import BtnComponent from "./Components/BtnComponent"
import { BASEURL } from "../Utils/urlUtils"

export default function SimResultPage(){

    const params = useParams()

    const dayValue = parseInt(params.day, 10)

    const isBellowZero = dayValue - 1 < 0
    const isMax = dayValue < 29

    const [data, setData] = useState({})

    useEffect(()=>{
        const fetchData = async()=>{
            const response = await fetch(`${BASEURL}/day_statistics/${dayValue}`)
            const dataJson = await response.json()
            setData(dataJson)
        }

        fetchData()
    }, [dayValue])

    return(
        <>
            <div className="flex gap-2">
                <BtnComponent isVisible={!isBellowZero} name={"Back"} day={dayValue-1}/>
                <div className="flex flex-col items-center w-8/12 h-screen">
                    <Link className=" flex text-xl justify-center items-center bg-black mt-2 text-white w-32 h-10 font-serif" to="/charts/">Charts</Link>
                    <ShowData day={dayValue} data={data}/>
                </div>
                <BtnComponent isVisible={isMax} name={"Next"} day={dayValue+1}/>
            </div>
        </>
    )
}