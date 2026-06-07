// GFSM v1 visualization example for Google Earth Engine.
// Public ImageCollection of approximately 17,000 30 m GFSM tile images.
var gfsmCollection = ee.ImageCollection('projects/floodsus/assets/fsm_ei5');

var gfsm = gfsmCollection.mosaic().select(0).rename('gfsm');
var validMask = gfsm.gte(1).and(gfsm.lte(5));
var gfsmMasked = gfsm.updateMask(validMask);

var classNames = [
  'Very Low',
  'Low',
  'Moderate',
  'High',
  'Very High'
];
var palette = ['2c7bb6', 'abd9e9', 'ffffbf', 'fdae61', 'd7191c'];

Map.setOptions('HYBRID');
Map.setCenter(90.4, 23.7, 7);
Map.addLayer(gfsmMasked, {min: 1, max: 5, palette: palette}, 'GFSM v1');

var legend = ui.Panel({
  style: {
    position: 'bottom-left',
    padding: '8px 12px'
  }
});

legend.add(ui.Label({
  value: 'GFSM v1 classes',
  style: {fontWeight: 'bold', margin: '0 0 6px 0'}
}));

for (var i = 0; i < classNames.length; i++) {
  var colorBox = ui.Label({
    style: {
      backgroundColor: '#' + palette[i],
      padding: '8px',
      margin: '0 6px 4px 0'
    }
  });
  var label = ui.Label({
    value: (i + 1) + ' - ' + classNames[i],
    style: {margin: '0 0 4px 0'}
  });
  legend.add(ui.Panel({
    widgets: [colorBox, label],
    layout: ui.Panel.Layout.Flow('horizontal')
  }));
}

Map.add(legend);
