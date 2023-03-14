import './style.css';
import React, {useState} from "react";

const policyDefaults = {
  "PanelMoves": ["Panel Moves", 0.02],
  "Homeless": ["Homeless", 0.04],
  "SocialServicesQuota": ["Social Services Quota", 0.04],
  "Transfer": ["Transfer", 0.01],
  "HomeScheme": ["Home Scheme", 0.04],
  "FirstTimeApplicants": ["First Time Applicants", 0.01],
  "TenantFinder": ["TenantFinder", 0.01],
  "Downsizer": ["Downsizer", 0.02],
  "Decants": ["Decants", 0.8],
  "Other": ["Other", 0.01]
};

const supplyDefaults = {
  "1": ["One Bedroom Properties", 58],
  "2": ["Two Bedroom Properties", 53],
  "3": ["Three Bedroom Properties", 29],
  "4": ["Four or More Bedroom Properties", 2]
};

const dateDefaults = {
  "startDate": ["Starting Date", "2022-01-01"],
  "endDate": ["End Date", "2022-12-31"]
}

function Settings() {
  const [policyInputs, setPolicyInputs] = useState(Object.values(policyDefaults));
  const [supplyInputs, setSupplyInputs] = useState(Object.values(supplyDefaults));
  const [dateInputs, setDateInputs] = useState(Object.values(dateDefaults));

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
      <h2>Application Policy Inputs</h2>
      {Object.entries(policyDefaults).map(([key, [name, value]], index) => (
        <div key={index}>
          <label htmlFor={`policy-input-${index}`}>{name}</label>
          <br/>
          <input
            id={`policy-input-${index}`}
            type="range"
            step="0.01"
            max="1"
            min="0"
            name={`policy-input-${index}`}
            value={policyInputs[index][1] || value}
            onChange={(e) => handlePolicyInputChange(index, e.target.value)}
          />
        </div>
      ))}

      <h2>Property Supply Inputs</h2>
      {Object.entries(supplyDefaults).map(([key, [name, value]], index) => (
        <div key={index}>
          <label htmlFor={`supply-input-${index}`}>{key}</label>
          <br/>
          <input
            id={`supply-input-${index}`}
            type="number"
            step="1"
            name={`supply-input-${index}`}
            value={supplyInputs[index][1] || value}
            onChange={(e) => handleSupplyInputChange(index, e.target.value)}
          />
        </div>

      ))}

      <h2>Date Inputs</h2>
      {Object.entries(dateDefaults).map(([key, [name, value]], index) => (
        <div key={index}>
          <label htmlFor={`date-input-${index}`}>{name}</label>
          <br/>
          <input
            name={`date-input-${index}`}
            id={`date-input-${index}`}
            type="date"
            value={dateInputs[index][1] || value}
            onChange={(e) => handleDateInputChange(index, e.target.value)}
          />
        </div>

      ))}

      <button type="submit">Submit</button>
    </form>
  );
}

export default Settings;