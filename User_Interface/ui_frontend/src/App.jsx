import { useState } from 'react'
import PotholeTarPrediction from './Pages/PotholeTarPrediction.jsx'
import { Router, Link, Route, BrowserRouter, Routes } from 'react-router-dom'
import Home from './Pages/Home.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
