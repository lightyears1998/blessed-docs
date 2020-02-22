# Picture

(Also check the new blessed [image implementation](https://github.com/chjj/blessed#image-from-box) which has several benefits over this one.)

![picture.png](https://github.com/yaronn/blessed-contrib/raw/master/docs/images/picture.png)

`````javascript
    var pic = contrib.picture(
       { file: './flower.png'
       , cols: 25
       , onReady: ready})
    function ready() {screen.render()}
`````

note: only png images are supported.
