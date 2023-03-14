import React, { Component } from 'react';
import ReactEcharts from 'echarts-for-react';

const Home = () => {

    const option = {
        title: {
            text: '',
        },
        tooltip: {},
        xAxis: {
            data: ['Band1', 'Band2', 'Band3', 'Band4', 'Ban5',]
        },
        yAxis: {},
        series: [
            {
                name: '',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20, 10],
            },
        ],
    };
    const avatarUrl = "logo.png"

    return (
        <>
            <ReactEcharts option={option}/>
        </>
    );

}

export default Home;
