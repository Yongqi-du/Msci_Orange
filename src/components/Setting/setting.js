import './style.css';
import React, {useState} from "react";

function Settings() {
    const [policyInputs, setPolicyInputs] = useState(Array(10).fill(0));
    const [supplyInputs, setSupplyInputs] = useState(Array(4).fill(0));
    const [dateInputs, setDateInputs] = useState(Array(2).fill(""));

    const handlePolicyInputChange = (index, value) => {
        const newPolicyInputs = [...policyInputs];
        newPolicyInputs[index] = parseFloat(value);
        setPolicyInputs(newPolicyInputs);
    };

    const handleSupplyInputChange = (index, value) => {
        const newSupplyInputs = [...supplyInputs];
        newSupplyInputs[index] = parseInt(value);
        setSupplyInputs(newSupplyInputs);
    };

    const handleDateInputChange = (index, value) => {
        const newDateInputs = [...dateInputs];
        newDateInputs[index] = value;
        setDateInputs(newDateInputs);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Policy Inputs: ", policyInputs);
        console.log("Supply Inputs: ", supplyInputs);
        console.log("Date Inputs: ", dateInputs);
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Policy Inputs</h2>
            {policyInputs.map((value, index) => (
                <input
                    key={index}
                    type="number"
                    step="0.01"
                    value={value}
                    onChange={(e) => handlePolicyInputChange(index, e.target.value)}
                />
            ))}

            <h2>Supply Inputs</h2>
            {supplyInputs.map((value, index) => (
                <input
                    key={index}
                    type="number"
                    step="1"
                    value={value}
                    onChange={(e) => handleSupplyInputChange(index, e.target.value)}
                />
            ))}

            <h2>Date Inputs</h2>
            {dateInputs.map((value, index) => (
                <input
                    key={index}
                    type="date"
                    value={value}
                    onChange={(e) => handleDateInputChange(index, e.target.value)}
                />
            ))}

            <button type="submit">Submit</button>
        </form>
    );
}

export default Settings;