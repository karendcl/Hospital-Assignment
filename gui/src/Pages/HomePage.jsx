import { BASEURL } from "../Utils/urlUtils"
import SettingsIcon from '@mui/icons-material/Settings';
import { useRef, useState } from "react";
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Modal from '@mui/material/Modal';
import LocalHospitalIcon from '@mui/icons-material/LocalHospital';
import { useNavigate } from "react-router-dom";
import Slider from '@mui/material/Slider';


const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4
};


export default function HomePage() {
  const navigate = useNavigate()
  const [open, setOpen]= useState(false)

  const icuBeds = useRef('10')
  const commonBeds = useRef('40')
  const lambdaValue = useRef('10')
  const amountPatiens = useRef('50')
  
  const handleClickSim=()=>{
    const startSim = async ()=>{
      const response = await fetch(`${BASEURL}/start_simulation?icu_beds=${icuBeds.current}&common_beds=${commonBeds.current}&lambda_=${lambdaValue.current}&n_patients=${amountPatiens.current}`)
      const data = await response.json()
    }

    startSim()
    navigate('/results/0')
  }

  return (
    <>
    <div className="flex flex-col items-center justify-center h-screen">
    <LocalHospitalIcon sx={{fontSize: 200 , color:'red', marginBottom: 'auto'}}></LocalHospitalIcon><h1 className=" text-7xl mb-16">Hospital Assignment Simulation</h1>
      <div className="flex mt-auto mb-auto gap-10">
        <Button className= "h-32 w-32 text-lg flex flex-col" variant="contained" onClick={handleClickSim}>
          <p className=" text-white">Start</p> <p className=" text-white">Simulation</p>
        </Button>
        <Button className="flex w-32 h-32" variant="contained" onClick={() => { setOpen(true) }}><SettingsIcon sx={{fontSize: 100}}></SettingsIcon></Button>
        <Modal
          open={open}
          onClose={() => { setOpen(false) }}
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
        >
          <Box sx={style}>
            <div className="flex">
              <p className=" text-md w-2/5 font-sans font-bold">ICU Beds</p>
              <Slider className="w-3/5" getAriaValueText={(value)=>{icuBeds.current = value}} defaultValue={10} aria-label="Default" valueLabelDisplay="auto" />
            </div>
            <div className="flex">
              <p className=" text-md w-2/5 font-sans font-bold">Common Beds</p>
              <Slider className="w-3/5" getAriaValueText={(value)=>{commonBeds.current = value}} defaultValue={40} aria-label="Default" valueLabelDisplay="auto" />
            </div>
            <div className="flex">
              <p className=" text-md w-2/5 font-sans font-bold">Lambda</p>
              <Slider className="w-3/5" getAriaValueText={(value)=>{lambdaValue.current = value}} defaultValue={10} aria-label="Default" valueLabelDisplay="auto" />
            </div>
            <div className="flex">
              <p className=" text-md w-2/5 font-sans font-bold">Amount of Patiens</p>
              <Slider className="w-3/5" getAriaValueText={(value)=>{amountPatiens.current = value}} defaultValue={50} aria-label="Default" valueLabelDisplay="auto" />
            </div>

            <div className="flex justify-center">
            <Button className="flex w-10 h-10" variant="contained" onClick={() => { setOpen(false) }}>Close</Button>
            </div>
          </Box>
        </Modal>
      
      </div>
      
    </div>
    </>
  )
}
