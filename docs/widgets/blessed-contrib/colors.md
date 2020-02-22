# Colors

You can use 256 colors ([source](https://github.com/yaronn/blessed-contrib/blob/master/examples/line-random-colors.js)):

`````javascript
  function randomColor() {
    return [Math.random() * 255,Math.random()*255, Math.random()*255]
  }

  line = contrib.line(
  {
    ...
    , style: { line: randomColor(), text: randomColor(), baseline: randomColor() }
  })
`````
