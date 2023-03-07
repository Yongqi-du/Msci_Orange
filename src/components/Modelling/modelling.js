import './style.css';
import { useEffect, useRef } from 'react';
import * as echarts from 'echarts';

function Modelling() {
  const chartRef = useRef(null);

  useEffect(() => {
    const chart = echarts.init(chartRef.current);
    const xAxisData = [];
    const data1 = [];
    const data2 = [];

    for (var i = 0; i < 100; i++) {
      xAxisData.push('A' + i);
      data1.push((Math.sin(i / 5) * (i / 5 - 10) + i / 6) * 5);
      data2.push((Math.cos(i / 5) * (i / 5 - 10) + i / 6) * 5);
    }

    const option = {
      title: {
        text: 'Bar Animation Delay'
      },
      legend: {
        data: ['bar', 'bar2']
      },
      toolbox: {
        // y: 'bottom',
        feature: {
          magicType: {
            type: ['stack']
          },
          dataView: {},
          saveAsImage: {
            pixelRatio: 2
          }
        }
      },
      tooltip: {},
      xAxis: {
        data: xAxisData,
        splitLine: {
          show: false
        }
      },
      yAxis: {},
      series: [
        {
          name: 'bar',
          type: 'bar',
          data: data1,
          emphasis: {
            focus: 'series'
          },
          animationDelay: function (idx) {
            return idx * 10;
          }
        },
        {
          name: 'bar2',
          type: 'bar',
          data: data2,
          emphasis: {
            focus: 'series'
          },
          animationDelay: function (idx) {
            return idx * 10 + 100;
          }
        }
      ],
      animationEasing: 'elasticOut',
      animationDelayUpdate: function (idx) {
        return idx * 5;
      }
    };

    chart.setOption(option);

    return () => {
      chart.dispose(); // clean up the chart when the component unmounts
    };
  }, []);

  return (
    <div className='flex-col'>
      <div className='h4'>
        Allocation Policy Modelling
      </div>
      <div className='flex-row'>
        <div ref={chartRef} style={{ width: '600px', height: '400px' }}></div>
      </div>
      <button>Submit</button>
    </div>
  );
}

export default Modelling;
