// import logo from './logo.svg';
// import button_circle from './assets/images/button-circle.png';


import React, { useState } from "react";

import './App.css';

import { FileUploader } from './components/FileUploader';
import Navbar from './components/Navbar/navbar';
import Main from './components/Main/main';
import Modelling from "./components/Modelling/modelling";
import Export from './components/Export/export';
import User from './components/User/user';
import Settings from "./components/Setting/setting";


// Comment out the next 3 lines when editing locally
import { Amplify } from 'aws-amplify';

import { withAuthenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';

import awsExports from './aws-exports';
Amplify.configure(awsExports);

function App({ signOut, user }) {

  const [showMain, setShowMain] = useState(false)
  const [showModel, setShowModel] = useState(false)
  const [showUpload, setShowUpload] = useState(false)
  const [showExport, setShowExport] = useState(false)
  const [showUser, setShowUser] = useState(false)
  const [showSettings, setShowSettings] = useState(false)

  const toggleMain = () => {
    setShowMain(!showMain);
    setShowModel(false);
    setShowUpload(false);
    setShowExport(false);
    setShowUser(false);
    setShowSettings(false);
  };

  const toggleModel = () => {
    setShowModel(!showModel);
    setShowMain(false);
    setShowUpload(false);
    setShowExport(false);
    setShowUser(false);
    setShowSettings(false);
  };
  
  const toggleUpload = () => {
    setShowUpload(!showUpload);
    setShowMain(false);
    setShowModel(false);
    setShowExport(false);
    setShowUser(false);
    setShowSettings(false);
  };
  
  const toggleExport = () => {
    setShowExport(!showExport);
    setShowMain(false);
    setShowModel(false);
    setShowUpload(false);
    setShowUser(false);
    setShowSettings(false);
  };
  
  const toggleUser = () => {
    setShowUser(!showUser);
    setShowMain(false);
    setShowModel(false);
    setShowUpload(false);
    setShowExport(false);
    setShowSettings(false);
  };
  
  const toggleSettings = () => {
    setShowSettings(!showSettings);
    setShowMain(false);
    setShowModel(false);
    setShowUpload(false);
    setShowExport(false);
    setShowUser(false);
  };
  

  return (
    <div className='desktop'>
      <Navbar toggleMain={toggleMain} toggleModel={toggleModel} toggleUpload={toggleUpload} toggleExport={toggleExport} toggleUser={toggleUser} toggleSettings={toggleSettings}/>
      {showMain ? <Main /> : null}
      {showUpload ? <FileUploader /> : null}
      {showExport ? <Export /> : null}
      {showModel ? <Modelling/> : null}
      {showUser ? <User/> : null}
      {showSettings ? <Settings/> : null}
    </div>
  );
}

export default withAuthenticator(App);

// function First(props) {
//   const {children, className } = props;

//   return (
//       <div className={`first ${className || ""}`}>
//           <div className="caption valign-text-middle inter-medium-baltic-sea-10-4px">{children}</div>
//       </div>
//   );
// }


// function RangeSlider(props) {
// const {rangeButtonProps } = props;

// return (
//   <div className='range-slider'>
//     <div className='overlap-group'>
//       <div className='range-track'></div>
//       <div className='dot'></div>
//       <div className='dot-1'></div>
//       <div className='dot-2'></div>
//       <div className='dot-3'></div>
//       <div className='dot-4'></div>
//       <div className='dot-5'></div>
//       <div className='dot-6'></div>
//       <div className='dot-7'></div>
//       <div className='dot-8'></div>
//       <div className='dot-9'></div>
//       <div className='dot-10'></div>
//       <div className='range-thumb'></div>
//       <RangeButton />
//       <RangeButton className={rangeButtonProps.className} />
//     </div>
//   </div>
// );
// }

// function RangeButton(props) {
// const { className } = props;

// return <div className={`range-button ${className || ""}`}></div>
// }

// function Axis(props) {
// const { valueL } = props;

// return (
//   <div className='axis'>
//     <div className='value-l valign-text-middle'>
//       {valueL}
//     </div>
//     <img className="x" src="" alt="X"/>
//   </div>
// );
// }

// const rangeButton2Data = {
// className: "range-button-1",
// };

// const rangeSliderData = {
// rangeButtonProps: rangeButton2Data,
// };