import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import HomePage from './Pages/HomePage.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import SimResultPage from './Pages/SimResultPage.jsx'


const router = createBrowserRouter([
  {
    path:'/',
    element:<HomePage/>
  },
  {
    path:'/results/:day',
    element:<SimResultPage/>
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <RouterProvider router={router}></RouterProvider>
  </React.StrictMode>,
)
