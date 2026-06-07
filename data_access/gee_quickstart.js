// GFSM v1 Google Earth Engine quickstart.
// Public ImageCollection of approximately 17,000 30 m GFSM tile images.
var gfsmCollection = ee.ImageCollection('projects/floodsus/assets/fsm_ei5');

var gfsm = gfsmCollection.mosaic().select(0).rename('gfsm');
var validMask = gfsm.gte(1).and(gfsm.lte(5));
var gfsmMasked = gfsm.updateMask(validMask);

var gfsmVis = {
  min: 1,
  max: 5,
  palette: ['2c7bb6', 'abd9e9', 'ffffbf', 'fdae61', 'd7191c']
};

Map.addLayer(gfsmMasked, gfsmVis, 'GFSM v1 susceptibility');
Map.setCenter(90.4, 23.7, 7);
