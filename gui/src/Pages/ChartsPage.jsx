import { Link } from "react-router-dom";
import BarChartComponent from "./Components/BarChartComponet";



export default function ChartsPage() {
    return(
        <>
        
        <div className="flex w-full">
            <div className="flex w-20 h-screen">
                <Link className="flex w-20 h-8 text-lg bg-black text-center justify-center text-white font-bold" to='/results/0'><p className="text-center">Back</p></Link>
            </div>
            <div className="flex flex-col w-6/12 h-screen overflow-auto">
                <BarChartComponent className="flex flex-col" color='' url_state={'deaths'} labelText={'Deaths'} title={'Daily Deaths'}></BarChartComponent>
                <BarChartComponent className="flex flex-col" color='#23A5A1' url_state={'cured'} labelText={'Cured'} title={'Daily Cured'}></BarChartComponent>            
            </div>
            <div className="flex flex-col w-6/12 h-screen overflow-auto">
                <BarChartComponent className="flex flex-col" color='#CF57DF' url_state={'better'} labelText={'Better'} title={'Daily Better'}></BarChartComponent>
                <BarChartComponent className="flex flex-col" color='#575CC6' url_state={'worse'} labelText={'Worse'} title={'Daily Worse'}></BarChartComponent>
            </div>
        </div>
        </>
    )
}
