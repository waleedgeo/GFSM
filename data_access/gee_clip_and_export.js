// Clip and export a GFSM v1 subset from Google Earth Engine.
// Public ImageCollection of approximately 17,000 30 m GFSM tile images.
var gfsmCollection = ee.ImageCollection('projects/floodsus/assets/fsm_ei5');

var gfsm = gfsmCollection.mosaic().select(0).rename('gfsm');
var validMask = gfsm.gte(1).and(gfsm.lte(5));

// Example AOI: central Bangladesh. Replace with your own geometry.
var aoi = ee.Geometry.Rectangle([89.8, 23.1, 91.1, 24.2]);
var clipped = gfsm.clip(aoi);

Map.centerObject(aoi, 8);
Map.addLayer(clipped.updateMask(validMask), {
  min: 1,
  max: 5,
  palette: ['2c7bb6', 'abd9e9', 'ffffbf', 'fdae61', 'd7191c']
}, 'GFSM v1 clipped');
Map.addLayer(aoi, {color: 'white'}, 'AOI');

Export.image.toDrive({
  image: clipped.updateMask(validMask).unmask(0).toByte(),
  description: 'GFSM_v1_clipped_export',
  folder: 'GFSM_v1',
  fileNamePrefix: 'gfsm_v1_clipped',
  region: aoi,
  scale: 30,
  maxPixels: 1e13
});
