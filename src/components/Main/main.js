import search from './search.png';
import container_1 from './container-1.png';
import numPerHousingBand from './NumberPerHousingBand.jpeg';

import './style.css';

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
                        <img src={numPerHousingBand} alt="Number Per Housing Band"/>
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

export default Main;