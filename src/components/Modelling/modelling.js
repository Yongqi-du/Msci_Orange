import './style.css';

import charts from './group project-6.png';
import edits from './group project-9.png';

function Modelling() {
    return (
        <div className='flex-col'>
            <div className='h4'>
                Allocation Policy Modelling
            </div>
            <div className='flex-row'>
                <img src={charts} alt="Charts"/>
                <img src={edits} alt="Edit Boxes"/>
            </div>
            <button>Submit</button>
        </div>
    )
};

export default Modelling;