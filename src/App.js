// import logo from './logo.svg';
// import button_circle from './assets/images/button-circle.png';
import search from './assets/images/search.png';
import container_1 from './assets/images/container-1.png';

import React, { useState } from "react";

import './App.css';

import { FileUploader } from './components/FileUploader';
import Navbar from './components/Navbar/navbar';

// import { Amplify } from 'aws-amplify';
// import awsExports from './aws-exports';
// Amplify.configure(awsExports);

function App() {

  const [showMain, setShowMain] = useState(false)
  const [showUpload, setShowUpload] = useState(false)

  const toggleMain = () => {
    setShowMain(!showMain);
  };

  const toggleUpload = () => {
    setShowUpload(!showUpload);
  };

  return (
    <div className='desktop'>
      <Navbar toggleMain={toggleMain} toggleUpload={toggleUpload}/>
      {/* <div style={{ display: 'flex', justifyContent: 'space-between' }}>
        <button onClick={() => setShowMain(true)}>Show Main </button>
        <button onClick={() => setShowUpload(true)}>Show Upload </button>
      </div> */}
      {showMain ? <Main /> : null}
      {showUpload ? <FileUploader /> : null}
    </div>
  );
}

export default App;

function Main() {

  return (
    <div className='flex-row'>
        <div className='navigation'>
          <div className='input-search'>
            <div className='search-master-dense'>
              <div className='body-1'>
                <img className='search' src={search} alt="search"/>
                <div className='caption-7 valign-text-middle'>
                  Search
                </div>
              </div>
            </div>
          </div>
          <TreeMaster caption="Status"/>
          <TreeMaster2 caption="Unoccupied"/>
          <TreeMaster2 caption="Occupied"/>
          <TreeMaster2 caption="Overoccupied"/>
          <TreeMaster2 caption="Underoccupied"/>
          <TreeMaster caption="Size"/>
          <TreeMaster2 caption="Studio"/>
          <TreeMaster2 caption="1-Bedroom"/>
          <TreeMaster2 caption="2-Bedrooms"/>
          <TreeMaster2 caption="3-Bedrooms"/>
        </div>
        <div className='flex-col'>
          <div className='h4'>
            Cost/Time
          </div>
          <p className='h6'>
            Dashboard with charts and metrics
          </p>
          <div className='overlap-group1'>
            <div className='bar-chart'>
              <div className='overlap-group'>
                <div className='grid inter0normal-topaz-10-4px'>
                  <div className='axis-1'>
                    <div className='value-l-1 valign-text-middle'>
                      15K
                    </div>
                    <img className='x-3' src="x.png" alt="x"/>
                  </div>
                  
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  )
}

// function First(props) {
//   const {children, className } = props;

//   return (
//       <div className={`first ${className || ""}`}>
//           <div className="caption valign-text-middle inter-medium-baltic-sea-10-4px">{children}</div>
//       </div>
//   );
// }

function TreeMaster (props) {
const { caption } = props;

return (
  <div className='tree-master'>
    <div className='tree'>
      <img className='container-l' src={container_1} alt='Container (L)'/>
      <div className='list-master'>
        <div className='caption-1 valign-txt-middle inter-medium-eerie-black-10-4px'>
          {caption}
        </div>
      </div>
    </div>
  </div>
);
}

function TreeMaster2 (props) {
const { caption } = props;

return (
  <div className='tree-master-1'>
    <div className='tree-1'>
      <img className='container-l-1' src={container_1} alt='Container (L)'/>
      <div className='list-master-1'>
        <div className='caption-2 valign-txt-middle inter-medium-eerie-black-10-4px'>
          {caption}
        </div>
      </div>
    </div>
  </div>
);
}

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