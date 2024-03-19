import { BarChart } from '@mui/x-charts/BarChart';
import { BASEURL } from '../../Utils/urlUtils';
import { useEffect, useState } from 'react';



export default function BarChartComponet({url_state, labelText, title, color, className}) {
    const chartSetting = {
        yAxis: [
          {
            label: labelText,
          },
        ],
        width: 600,
        height: 350,
      };

    const valueFormatter = (value) => `${value} ${labelText}`;

    const [data, setData] = useState(undefined)

    useEffect(()=>{
        fetch(`${BASEURL}/stats/` + `${url_state}`)
            .then(r=> r.json())
            .then(d=> setData(d))
    },[])

    const isArray = Array.isArray(data)

    let dataset = isArray? data.map((x, i) => {
        return {
          day: `${i+1}`,
          value: Number(x),
        };
     }) : []
  return (
    <>
    {isArray && <BarChart className={className}
      dataset={dataset}
      xAxis={[{ scaleType: 'band', dataKey: 'day' }]}
      series={[{ dataKey: 'value', label: title, valueFormatter, color: color }]}
      {...chartSetting}
    />}
    </>
  );
}