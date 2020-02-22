# Donut

![donut.gif](https://github.com/yaronn/blessed-contrib/raw/master/docs/images/donut.gif)

`````javascript
  var donut = contrib.donut({
    label: 'Test',
    radius: 8,
    arcWidth: 3,
    remainColor: 'black',
    yPadding: 2,
    data: [
      {percent: 80, label: 'web1', color: 'green'}
    ]
  });
`````

Data passed in uses `percent` and `label` to draw the donut graph. Color is optional and defaults to green.

`````javascript
  donut.setData([
    {percent: 87, label: 'rcp','color': 'green'},
    {percent: 43, label: 'rcp','color': 'cyan'},
  ]);
`````

Updating the donut is as easy as passing in an array to `setData` using the same array format as in the constructor. Pass in as many objects to the array of data as you want, they will automatically resize and try to fit. However, please note that you will still be restricted to actual screen space.
