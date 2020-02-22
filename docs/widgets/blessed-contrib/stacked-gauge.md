# Stacked Gauge

![stackgauge.gif](https://github.com/yaronn/blessed-contrib/raw/master/docs/images/stackgauge.gif)

Either specify each stacked portion with a `percent` and `stroke`...

`````javascript
   var gauge = contrib.gauge({label: 'Stacked '})
   gauge.setStack([{percent: 30, stroke: 'green'}, {percent: 30, stroke: 'magenta'}, {percent: 40, stroke: 'cyan'}])
`````

Or, you can just supply an array of numbers and random colors will be chosen.

`````javascript
   var gauge = contrib.gauge({label: 'Stacked Progress'})
   gauge.setStack([30,30,40])
`````
