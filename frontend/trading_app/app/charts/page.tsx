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
  //console.log(data)
  const content = (
    <section>
       <Chart/>
    </section>
  )
  
  return content;
}
