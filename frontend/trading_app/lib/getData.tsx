import { RSC } from 'next/dist/client/components/app-router-headers'
import React from 'react'

export default async function getData() {
    const res = await fetch('http://127.0.0.1:5000/count')
    
    if(!res.ok) throw new Error('failed to fetch data')
    const data = await res.json()
    return data
}
