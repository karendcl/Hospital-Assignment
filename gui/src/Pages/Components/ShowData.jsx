

export default function ShowData({day, data}){
    return(
        <>
            <h1 className="text-6xl pt-3 pb-8">Day {day}</h1>
            <div className="flex w-4/5 h-4/5 bg-slate-100 border-2 border-black">
                <div className="flex flex-col w-1/2 text-lg gap-2 pr-16 pl-16 pt-5">
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Initial Critical Patients: </p> <p className="flex font-semibold">{data.initial_critical_patients}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Initial Grave Patients: </p>    <p className="flex font-semibold">{data.initial_grave_patients}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Initial Regular Patients: </p>  <p className="flex font-semibold">{data.initial_regular_patients}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">New Critical Patients: </p>     <p className="flex font-semibold">{data.new_critical_patients}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">New Grave Patients: </p>        <p className="flex font-semibold">{data.new_grave_patients}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">New Regular Patients: </p>      <p className="flex font-semibold">{data.new_regular_patients}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Final Critical Patients: </p>   <p className="flex font-semibold">{data.final_critical_patients}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Final Grave Patients: </p>      <p className="flex font-semibold">{data.final_grave_patients}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Final Regular Patients: </p>    <p className="flex font-semibold">{data.final_regular_patients}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Critical Patients Cured: </p>   <p className="flex font-semibold">{data.critical_patients_cured}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Grave Patients Cured: </p>      <p className="flex font-semibold">{data.grave_patients_cured}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Regular Patients Cured: </p>    <p className="flex font-semibold">{data.regular_patients_cured}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Critical Patients Died: </p>    <p className="flex font-semibold">{data.critical_patients_died}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Grave Patients Cured: </p>      <p className="flex font-semibold">{data.grave_patients_died}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Regular Patients Cured: </p>    <p className="flex font-semibold">{data.regular_patients_died}</p></div>
                </div>
                <div className="flex flex-col w-1/2 text-lg gap-2 pr-16 pl-16 pt-5">
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Critical to Grave: </p>   <p className="flex font-semibold">{data.critical_to_grave}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Critical to Regular: </p> <p className="flex font-semibold">{data.critical_to_regular}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Grave to Critical: </p>   <p className="flex font-semibold">{data.grave_to_critical}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Grave to Regular: </p>    <p className="flex font-semibold">{data.grave_to_regular}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Regular to Critical: </p> <p className="flex font-semibold">{data.regular_to_critical}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Regular to Grave: </p>    <p className="flex font-semibold">{data.regular_to_grave}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Critical ICU: </p>        <p className="flex font-semibold">{data.critical_ICU}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Critical Commom: </p>     <p className="flex font-semibold">{data.critical_common}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Critical None: </p>       <p className="flex font-semibold">{data.critical_none}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Grave ICU: </p>           <p className="flex font-semibold">{data.grave_ICU}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Garve Commom: </p>        <p className="flex font-semibold">{data.grave_common}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Grave None: </p>          <p className="flex font-semibold">{data.grave_none}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Regular ICU: </p>         <p className="flex font-semibold">{data.regular_ICU}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Regular Common: </p>      <p className="flex font-semibold">{data.regular_common}</p></div>
                    <div className="flex flex-row justify-between"><p className="flex font-extrabold font-serif">Regular None: </p>        <p className="flex font-semibold">{data.regular_none}</p></div>
                </div>
            </div>
        </>
    )
}