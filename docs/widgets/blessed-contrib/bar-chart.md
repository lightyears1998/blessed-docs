# Bar Chart

![bar.gif](https://github.com/yaronn/blessed-contrib/raw/master/docs/images/bar.gif)

`````javascript
    var bar = contrib.bar(
       { label: 'Server Utilization (%)'
       , barWidth: 4
       , barSpacing: 6
       , xOffset: 0
       , maxHeight: 9})
    screen.append(bar) //must append before setting data
    bar.setData(
       { titles: ['bar1', 'bar2']
       , data: [5, 10]})
`````
