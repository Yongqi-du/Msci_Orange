import './style.css';
import React, {useState} from "react";

const policyDefaults = {
  "Panel Moves": 0.02,
  "Homeless": 0.04,
  "Social Services Quota": 0.04,
  "Transfer": 0.01,
  "Home Scheme": 0.04,
  "First Time Applicants": 0.01,
  "Tenant Finder": 0.01,
  "Downsizer": 0.02,
  "Decants": 0.8,
  "Other": 0.01
};

const supplyDefaults = {
  "One Bedroom Properties": 58,
  "Two Bedroom Properties": 53,
  "Three Bedroom Properties": 29,
  "Four+ Bedroom Properties": 2
};

const dateDefaults = {
  "startDate": "2022-01-01",
  "endDate": "2022-12-31"
}

function Settings() {
  const [policyInputs, setPolicyInputs] = useState(Object.values(policyDefaults).fill(0));
  const [supplyInputs, setSupplyInputs] = useState(Object.values(supplyDefaults).fill(0));
  const [dateInputs, setDateInputs] = useState(Object.values(dateDefaults).fill(""));

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
      {Object.entries(policyDefaults).map(([key, value], index) => (
        <div key={index}>
          <label htmlFor={`policy-input-${index}`}>{key}</label>
          <input
            id={`policy-input-${index}`}
            type="number"
            step="0.01"
            name={`policy-input-${index}`}
            value={policyInputs[index] || value}
            onChange={(e) => handlePolicyInputChange(index, e.target.value)}
          />
        </div>
      ))}

      <h2>Supply Inputs</h2>
      {Object.entries(supplyDefaults).map(([key, value], index) => (
        <div key={index}>
          <label htmlFor={`supply-input-${index}`}>{key}</label>
          <input
            id={`supply-input-${index}`}
            type="number"
            step="1"
            name={`supply-input-${index}`}
            value={supplyInputs[index] || value}
            onChange={(e) => handleSupplyInputChange(index, e.target.value)}
          />
        </div>

      ))}

      <h2>Date Inputs</h2>
      {Object.entries(dateDefaults).map(([key, value], index) => (
        <div key={index}>
          <label htmlFor={`date-input-${index}`}>{key}</label>
          <input
            name={`date-input-${index}`}
            id={`date-input-${index}`}
            type="date"
            value={dateInputs[index] || value}
            onChange={(e) => handleDateInputChange(index, e.target.value)}
          />
        </div>

      ))}

      <button type="submit">Submit</button>
    </form>
  );
}

export default Settings;