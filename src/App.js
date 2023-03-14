import 'antd/dist/reset.css';
 
 
import{ HashRouter } from 'react-router-dom'

import './App.css';
import { BrowserRouter as Router, Route,Routes } from 'react-router-dom';

import Export from '././components/Export/Export';
import FileUpload from "././components/FileUpload/FileUpload";
import Home from '././components/Home/Home';
import BasicLayout from "././components/BasicLayout/BasicLayout";
import Modelling from '././components/Modelling/Modelling';
import User from '././components/User/User';

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

export default App;
// export default withAuthenticator(App);