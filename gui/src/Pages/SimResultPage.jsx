import { useEffect, useState } from "react"
import { useParams, Link } from "react-router-dom"
import LinkComponent from "./Components/LinkComponent"
import ShowData from "./Components/ShowData"

const BASEURL='http://127.0.0.1:8000'

export default function SimResultPage(){

    const params = useParams()
    
    let isResponseOk = true

    const dayValue = parseInt(params.day, 10)

    const isZero = dayValue - 1 == 0

    const [data, setData] = useState([])

    useEffect(()=>{
        const fetchData = async()=>{
            const response = await fetch(`${BASEURL}/day_statistics/${dayValue}`)
            isResponseOk = response.ok
            console.log(isResponseOk)
            const dataJson = await response.json()
            setData(dataJson)
        }

        fetchData()
    }, [dayValue])

    return(
        <>
            <div className="flex gap-2">
                <div className=" flex items-center justify-center  w-2/12 h-screen ">
                    {!isZero && <LinkComponent day={dayValue-1} name="Back"/>}
                </div>
                <div className="flex flex-col items-center w-8/12 h-screen">
                    <ShowData day={dayValue} data={data}/>
                </div>
                <div className="flex items-center justify-center w-2/12 h-screen">
                    <LinkComponent day={dayValue+1} name="Next"/>   
                </div>
                
            </div>
        </>
    )
}