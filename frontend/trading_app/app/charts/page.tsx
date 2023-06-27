import type { Metadata } from "next";
import React from 'react' 
import getData from "@/lib/getData";
import { Chart } from "../components/Chart";

export const metadata: Metadata ={
    title: 'Charts',
}


export default async function ChartPage() {
  const data = await getData()
  //const data = await chart_data
  data.Rows.reverse();
  console.log(data.Rows[0][0].substring(0,10))
  const chart_data = data.Rows.map(
    (item:any) =>{
      return{
      time: item[0].substring(0,10),
      value: item[1],
      };
    }
  );
  const content = (
    <section>
       <Chart initialData={chart_data}/>
    </section>
  )
  
  return content;
}
