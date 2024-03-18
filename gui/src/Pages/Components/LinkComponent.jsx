import { Link } from "react-router-dom"

export default function LinkComponent({day, name}){
    return(
        <Link className="text-4xl text-center w-32 h-12 text-black" key={day} to={`/results/${day}`}>{name}</Link>
    )
}