

export default function ShowData({day, data}){

    const dataValue1 = [{prop:"Initial Critical Patients:", value: data.initial_critical_patients},
                        {prop:"Initial Grave Patients:", value: data.initial_grave_patients},
                        {prop:"Initial Regular Patients:", value: data.initial_regular_patients},
                        {prop:"New Critical Patients:", value: data.new_critical_patients},
                        {prop:"New Grave Patients:", value: data.new_grave_patients},
                        {prop:"New Regular Patients:", value: data.new_regular_patients},
                        {prop:"Final Critical Patients:", value: data.final_critical_patients},
                        {prop:"Final Grave Patients:", value: data.final_grave_patients},
                        {prop:"Final Regular Patients:", value: data.final_regular_patients},
                        {prop:"Critical Patients Cured:", value: data.critical_patients_cured},
                        {prop:"Grave Patients Cured:", value: data.grave_patients_cured},
                        {prop:"Regular Patients Cured:", value: data.regular_patients_cured},
                        {prop:"Critical Patients Died:", value: data.critical_patients_died},
                        {prop:"Grave Patients Died:", value: data.grave_patients_died},
                        {prop:"Regular Patients Died:", value: data.regular_patients_died}]

    const dataValue2 =[{prop:"Critical to Grave:", value: data.critical_to_grave},
                        {prop:"Critical to Regular:", value: data.critical_to_regular},
                        {prop:"Grave to Critical:", value: data.grave_to_critical},
                        {prop:"Grave to Regular:", value: data.grave_to_regular},
                        {prop:"Regular to Critical:", value: data.regular_to_critical},
                        {prop:"Regular to Grave:", value: data.regular_to_grave},
                        {prop:"Critical ICU:", value: data.critical_ICU},
                        {prop:"Critical Common:", value: data.critical_common},
                        {prop:"Critical None:", value: data.critical_none},
                        {prop:"Grave ICU:", value: data.grave_ICU},
                        {prop:"Grave Common:", value: data.grave_common},
                        {prop:"Grave None:", value: data.grave_none},
                        {prop:"Regular ICU:", value: data.regular_ICU},
                        {prop:"Regular Common:", value: data.regular_common},
                        {prop:"Regular None:", value: data.regular_none}]

    const dataValue1Mapped = dataValue1.map(x=>
        <div className="flex flex-row justify-between">
            <p className="flex font-extrabold font-serif">{x.prop} </p> 
            <p className="flex font-semibold">{x.value}</p>
        </div>
        )
    const dataValue2Mapped = dataValue2.map(x=>
         <div className="flex flex-row justify-between">
            <p className="flex font-extrabold font-serif">{x.prop} </p> 
            <p className="flex font-semibold">{x.value}</p>
        </div>
        )

    return(
        <>
            <h1 className="text-6xl pt-3 pb-4">Day {day+1}</h1>
            <div className="flex w-4/5 h-4/5 bg-slate-100 border-2 border-black overflow-auto">
                <div className="flex flex-col w-1/2 text-lg gap-2 pr-16 pl-16 pt-5">
                    {dataValue1Mapped}
                </div>
                <div className="flex flex-col w-1/2 text-lg gap-2 pr-16 pl-16 pt-5">
                    {dataValue2Mapped}
                </div>
            </div>
        </>
    )
}