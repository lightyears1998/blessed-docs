# Grid

A grid layout can auto position your elements in a grid layout.
When using a grid, you should not create the widgets, rather specify to the grid which widget to create and with which params.
Each widget can span multiple rows and columns.

`````javascript
   var screen = blessed.screen()

   var grid = new contrib.grid({rows: 12, cols: 12, screen: screen})

   //grid.set(row, col, rowSpan, colSpan, obj, opts)
   var map = grid.set(0, 0, 4, 4, contrib.map, {label: 'World Map'})
   var box = grid.set(4, 4, 4, 4, blessed.box, {content: 'My Box'})

   screen.render()
`````
