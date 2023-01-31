import React from "react";
// import { NavLink } from "react-router-dom";

import './style.css';

import button_circle from './button-circle.png';

function Navbar( {toggleMain, toggleUpload} ) {
  return (
    <div className='navbar'>
        <div className='logo-hamburger'>
          <img className='button-circle' src={button_circle} alt='Button Circle'/>
          <div className='name valign-text-middle'>
            Dashboard
          </div>
        </div>
        <div className="tabs-segmented">
          <div className='tabs-segmented-item' onClick={toggleMain}>
            <div className="first">
                <div className='caption-3 valign-text-middle inter-normal-topaz-10-4px'>
                    Home
                </div>
            </div>
          </div>
          
          <div className='tabs-segmented-item' onClick={toggleUpload}>
            <div className='caption-3 valign-text-middle inter-normal-topaz-10-4px'>
              Load Data
            </div>
          </div>
          <div className='tabs-segmented-item'>
            <div className='caption-3 valign-text-middle inter-normal-topaz-10-4px'>
              Export
            </div>
          </div>
        </div>
        <div className='right-userlist'>
          <div className='list'>
            <div className='list-master-2'>
              <div className="caption-5 valign-text-middle inter-normal-eerie-black-10-4px">
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
  );
}

export default Navbar;
