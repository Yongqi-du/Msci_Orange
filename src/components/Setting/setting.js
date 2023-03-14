import './style.css';
import React, {useState} from "react";

const policyDefaults = {
  "PanelMoves": 0.02,
  "Homeless": 0.04,
  "SocialServicesQuota": 0.04,
  "Transfer": 0.01,
  "HomeScheme": 0.04,
  "FirstTimeApplicants": 0.01,
  "TenantFinder":  0.01,
  "Downsizer": 0.02,
  "Decants": 0.8,
  "Other": 0.01
};

const policyLabelNames = {
  "PanelMoves": "Panel Moves",
  "Homeless": "Homeless",
  "SocialServicesQuota": "Social Services Quota",
  "Transfer": "Transfer",
  "HomeScheme": "Home Scheme",
  "FirstTimeApplicants": "First Time Applicants",
  "TenantFinder": "Tenant Finder",
  "Downsizer": "Downsizer",
  "Decants": "Decants",
  "Other": "Other"
};

const supplyDefaults = {
  "1": 58,
  "2": 53,
  "3": 29,
  "4": 2
};

const supplyLabelNames = {
  "1": "One Bedroom Properties",
  "2": "Two Bedroom Properties",
  "3": "Three Bedroom Properties",
  "4": "Four or More Bedroom Properties"
}

const dateDefaults = {
  "startDate": "2022-01-01",
  "endDate": "2022-12-31"
}

const dateLabelNames = {
  "startDate": "Starting Date",
  "endDate": "End Date"
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
    console.log("Policy Inputs: ", policyInputs);
    console.log("Supply Inputs: ", supplyInputs);
    console.log("Date Inputs: ", dateInputs);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Application Policy Inputs</h2>
      {Object.entries(policyDefaults).map(([key, value], index) => (
        <div key={index}>
          <label htmlFor={`policy-input-${index}`}>{policyLabelNames[key]}</label>
          <br/>
          <input
            id={`policy-input-${index}`}
            type="range"
            step="0.01"
            max="1"
            min="0"
            name={`policy-input-${index}`}
            value={policyInputs[index] || value}
            onChange={(e) => handlePolicyInputChange(index, e.target.value)}
          />
          <label htmlFor={`policy-input-${index}`}>{policyInputs[index] || value}</label>
        </div>
      ))}

      <h2>Property Supply Inputs</h2>
      {Object.entries(supplyDefaults).map(([key, value], index) => (
        <div key={index}>
          <label htmlFor={`supply-input-${index}`}>{supplyLabelNames[key]}</label>
          <br/>
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
      {Object.entries(dateDefaults).map(([key,  value], index) => (
        <div key={index}>
          <label htmlFor={`date-input-${index}`}>{dateLabelNames[key]}</label>
          <br/>
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