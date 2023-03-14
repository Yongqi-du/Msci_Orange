import 'antd/dist/reset.css';
 
 
import{ HashRouter } from 'react-router-dom'

import './App.css';
import { BrowserRouter as Router, Route,Routes } from 'react-router-dom';

// import Export from './components/Export/Export';
import FileUpload from './components/FileUpload/FileUpload';
import Home from './components/Home/Home';
import BasicLayout from "./components/BasicLayout/BasicLayout";
import Modelling from './components/Modelling/Modelling';
import User from './components/User/User';

// // Comment out the next 3 lines when editing locally
import { Amplify } from 'aws-amplify';

import { withAuthenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';

import awsExports from './aws-exports';
Amplify.configure(awsExports);


function App(){
    
  return(
    <Router>
    <div className = "App">
    <BasicLayout />
 
    
    </div>
    </Router>

  )
}


export default withAuthenticator(App);





// import React, { useState } from "react";

// import './App.css';

// import { FileUploader } from './components/FileUploader';

// import Layout from ''

// import Navbar from './components/Navbar/navbar';
// import Main from './components/Home/Home';
// import Modelling from "./components/Modelling/modelling";
// import Export from './components/Export/export';
// import User from './components/User/user';
// import Settings from "./components/Setting/setting";


// // Comment out the next 3 lines when editing locally
// import { Amplify } from 'aws-amplify';

// import { withAuthenticator } from '@aws-amplify/ui-react';
// import '@aws-amplify/ui-react/styles.css';

// import awsExports from './aws-exports';
// Amplify.configure(awsExports);

// function App({ signOut, user }) {

//   const [showMain, setShowMain] = useState(false)
//   const [showModel, setShowModel] = useState(false)
//   const [showUpload, setShowUpload] = useState(false)
//   const [showExport, setShowExport] = useState(false)
//   const [showUser, setShowUser] = useState(false)
//   const [showSettings, setShowSettings] = useState(false)

//   const toggleMain = () => {
//     setShowMain(!showMain);
//     setShowModel(false)
//     setShowUpload(false)
//     setShowExport(false)
//     setShowUser(false)
//     setShowSettings(false)
//   };

//   const toggleModel = () => {
//     setShowModel(!showModel);
//     setShowMain(false);
//     setShowUpload(false);
//     setShowExport(false);
//     setShowUser(false);
//     setShowSettings(false);
//   };
  
//   const toggleUpload = () => {
//     setShowUpload(!showUpload);
//     setShowMain(false);
//     setShowModel(false);
//     setShowExport(false);
//     setShowUser(false);
//     setShowSettings(false);
//   };
  
//   const toggleExport = () => {
//     setShowExport(!showExport);
//     setShowMain(false);
//     setShowModel(false);
//     setShowUpload(false);
//     setShowUser(false);
//     setShowSettings(false);
//   };
  
//   const toggleUser = () => {
//     setShowUser(!showUser);
//     setShowMain(false);
//     setShowModel(false);
//     setShowUpload(false);
//     setShowExport(false);
//     setShowSettings(false);
//   };
  
//   const toggleSettings = () => {
//     setShowSettings(!showSettings);
//     setShowMain(false);
//     setShowModel(false);
//     setShowUpload(false);
//     setShowExport(false);
//     setShowUser(false);
//   };
  

//   return (
//     <div className='desktop'>
//       <Navbar toggleMain={toggleMain} toggleModel={toggleModel} toggleUpload={toggleUpload} toggleExport={toggleExport} toggleUser={toggleUser} toggleSettings={toggleSettings}/>
//       {showMain ? <Main /> : null}
//       {showUpload ? <FileUploader /> : null}
//       {showExport ? <Export /> : null}
//       {showModel ? <Modelling/> : null}
//       {showUser ? <User/> : null}
//       {showSettings ? <Settings/> : null}
//     </div>
//   );
// }

// export default withAuthenticator(App);

