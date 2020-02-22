# Line Chart

![line.gif](https://github.com/yaronn/blessed-contrib/raw/master/docs/images/line.gif)

`````javascript
   var line = contrib.line(
         { style:
           { line: "yellow"
           , text: "green"
           , baseline: "black"}
         , xLabelPadding: 3
         , xPadding: 5
         , showLegend: true
         , wholeNumbersOnly: false //true=do not show fraction in y axis
         , label: 'Title'})
   var series1 = {
         title: 'apples',
         x: ['t1', 't2', 't3', 't4'],
         y: [5, 1, 7, 5]
      }
   var series2 = {
         title: 'oranges',
         x: ['t1', 't2', 't3', 't4'],
         y: [2, 1, 4, 8]
      }
   screen.append(line) //must append before setting data
   line.setData([series1, series2])
`````

**Examples:** [simple line chart](./examples/line-fraction.js), [multiple lines](./examples/multi-line-chart.js), [256 colors](./examples/line-random-colors.js)
