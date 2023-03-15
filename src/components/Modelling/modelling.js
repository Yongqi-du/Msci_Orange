import React, {Component, useState} from 'react';
import ReactEcharts from 'echarts-for-react';
import {View} from "@aws-amplify/ui-react";
import {API} from "aws-amplify";

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

const Modelling = () => {
    const option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['New', 'Queued', 'Resolved']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            axisTick: {
              show: false
            },
            data: ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10', '2022-01-11', '2022-01-12', '2022-01-13', '2022-01-14', '2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18', '2022-01-19', '2022-01-20', '2022-01-21']
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],

        series: [
          {
            name: 'New',
            type: 'bar',
            label: {
              show: true,
              position: 'inside'
            },
            emphasis: {
              focus: 'series'
            },
            data: [200, 170, 240, 244, 200, 220, 210,200, 170, 240, 244, 200, 220, 210,200, 170, 240, 244, 200, 220, 210]
          },

          {
            name: 'Resolved',
            type: 'bar',
            stack: 'Total',
            label: {
              show: true
            },
            emphasis: {
              focus: 'series'
            },
            data: [320, 302, 341, 374, 390, 450, 420,320, 302, 341, 374, 390, 450, 420,320, 302, 341, 374, 390, 450, 420]
          },

          {
            name: 'Queued',
            type: 'bar',
            stack: 'Total',
            label: {
              show: true,
              position: 'left'
            },
            emphasis: {
              focus: 'series'
            },
            data: [-120, -132, -101, -134, -190, -230, -210,-120, -132, -101, -134, -190, -230, -210,-120, -132, -101, -134, -190, -230, -210,-120, -132, -101, -134, -190, -230, -210,-120, -132, -101, -134, -190, -230, -210,-120, -132, -101, -134, -190, -230, -210]
          }
        ]
      };
    return (
      <View>
        <ReactEcharts option={option}/>
        <PolicyForm/>
      </View>
    );
}

function PolicyForm() {
  const [policyInputs, setPolicyInputs] = useState(Object.values(policyDefaults));
  const [supplyInputs, setSupplyInputs] = useState(Object.values(supplyDefaults));
  const [dateInputs, setDateInputs] = useState(Object.values(dateDefaults));

  const handlePolicyInputChange = (index, value) => {
    const newPolicyInputs = [...policyInputs];
    newPolicyInputs[index] = parseFloat(value);
    setPolicyInputs(newPolicyInputs);
    policyDefaults[index] = newPolicyInputs[index];
  };

  const handleSupplyInputChange = (index, value) => {
    const newSupplyInputs = [...supplyInputs];
    newSupplyInputs[index] = parseInt(value);
    setSupplyInputs(newSupplyInputs);
    supplyDefaults[index] = newSupplyInputs[index];
  };

  const handleDateInputChange = (index, value) => {
    const newDateInputs = [...dateInputs];
    newDateInputs[index] = value;
    setDateInputs(newDateInputs);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    let outputObj = {
      "policy": {},
      "supply": {},
      "startDate": "",
      "endDate": ""
    };

    outputObj["policy"] = policyDefaults;
    outputObj["supply"] = supplyDefaults;

    outputObj["startDate"] = dateInputs[0];
    outputObj["endDate"] = dateInputs[1];

    // try {
    //   const response = await API.post(
    //     "restapimodeller",
    //     "/modeller-api",
    //     {
    //       body: {outputObj}
    //     }
    //   );
    //   console.log(response);
    // } catch (error) {
    //   console.log(error);
    // }
    console.log(outputObj);
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
      <br/>
      <button type="submit" id="policy-form-submit">Submit</button>
    </form>
  );
}

export default Modelling;

