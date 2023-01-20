import logo from './logo.svg';
import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
import React from "react";

function App() {
    return (
        <div className="desktop">
          <div className='navbar'>
            <div className='logo-hamburger'>
              <img className='button-circle' src={logo} alt="Button Circle"/>
              <div className='name valign-text-middle'>
                Dashboard
              </div>
            </div>
            <div className='tabs-segmented'>
              <First>Home</First>
              <div className='second'>
                <div className='caption-3 valign-text-middle inter-normal-topaz-10-4px'>
                  Load Data
                </div>
              </div>
              <div className='third'>
                <div className='caption-3 valign-text-middle inter-normal-topaz-10-4px'>
                  Export
                </div>
              </div>
              <div className='right-userlist'>
                <div className='list'>
                  <div className='list-master-2'>
                    <div className='caption-5 valign-text-middle inter-normal-eerie-black-10-4px'>
                      David Hill
                    </div>
                  </div>
                </div>
                <div className='button-default'>
                  <div className='body'>
                    <div className='caption-6 valign-text-middle'>
                      Settings
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className='flex-row'>
              <div className='navigation'>
                <div className='input-search'>
                  <div className='search-master-dense'>
                    <div className='body-1'>
                      <img className='search' src={logo} alt='search'/>
                      <div className='caption-7 valign-text-middle'>
                        Search dense input
                      </div>
                    </div>
                  </div>
                </div>
                <TreeMaster caption="Status"/>
                <TreeMaster2 caption="Unoccupied"/>
                <TreeMaster2 caption="Occupied"/>
                <TreeMaster2 caption="Overcrowded"/>
                <TreeMaster2 caption="Underused"/>
                <TreeMaster caption="Size"/>
                <div clasname="tree-master-2">
                  <div className='tree-2'>
                    <img className="container-1-2" src={logo} alt="Container (L)"/>
                    <div className='list-master-3'>
                      <img className="caption-8" src={logo} alt="Caption"/>
                    </div>
                  </div>
                </div>
                <TreeMaster2 caption="Studio"/>
                <TreeMaster2 caption="1-Bedroom"/>
                <TreeMaster2 caption="2-Bedroom"/>
                <TreeMaster2 caption="3-Bedroom"/>
              </div>
              <div className="flex-col">
                <div className='h4'>
                  Cost/Time
                </div>
                <p className='h6'>
                  Dashboard with charts and metrics
                </p>
                <div className='breadcrumbs'>
                  <img className='collapse-left' src='collapse-left.svg' alt="Collapse Left"/>
                </div>
              </div>
            </div>
          </div>
        </div>
    );
}

export default App;

function First(props) {
    const {children, className } = props;

    return (
        <div className={`first ${className || ""}`}>
            <div className="caption valign-text-middle inter-medium-baltic-sea-10-4px">{children}</div>
        </div>
    );
}

function TreeMaster (props) {
  const { caption } = props;

  return (
    <div className='tree-master'>
      <div className='tree'>
        <img className='container-l' src={logo} alt='Container (L)'/>
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
        <img className='container-l-1' src={logo} alt='Container (L)'/>
        <div className='list-master-1'>
          <div className='caption-2 valign-txt-middle inter-medium-eerie-black-10-4px'>
            {caption}
          </div>
        </div>
      </div>
    </div>
  );
}

function RangeSlider(props) {
  const {rangeButtonProps } = props;

  return (
    <div className='range-slider'>
      <div className='overlap-group'>
        <div className='range-track'></div>
        <div className='dot'></div>
        <div className='dot-1'></div>
        <div className='dot-2'></div>
        <div className='dot-3'></div>
        <div className='dot-4'></div>
        <div className='dot-5'></div>
        <div className='dot-6'></div>
        <div className='dot-7'></div>
        <div className='dot-8'></div>
        <div className='dot-9'></div>
        <div className='dot-10'></div>
        <div className='range-thumb'></div>
        <RangeButton />
        <RangeButton className={rangeButtonProps.className} />
      </div>
    </div>
  );
}

function RangeButton(props) {
  const { className } = props;

  return <div className={`range-button ${className || ""}`}></div>
}

function Axis(props) {
  const { valueL } = props;

  return (
    <div className='axis'>
      <div className='value-l valign-text-middle'>
        {valueL}
      </div>
      <img className="x" src="" alt="X"/>
    </div>
  );
}

const rangeButton2Data = {
  className: "range-button-1",
};

const rangeSliderData = {
  rangeButtonProps: rangeButton2Data,
};