// Calculate GFSM v1 area by class within a user-defined AOI.
// Public ImageCollection of approximately 17,000 30 m GFSM tile images.
var gfsmCollection = ee.ImageCollection('projects/floodsus/assets/fsm_ei5');

var gfsm = gfsmCollection.mosaic().select(0).rename('gfsm');
var validMask = gfsm.gte(1).and(gfsm.lte(5));

// Example AOI: central Bangladesh. Replace with your own geometry.
var aoi = ee.Geometry.Rectangle([89.8, 23.1, 91.1, 24.2]);
var classes = ee.List.sequence(1, 5);

var areaImage = ee.Image.pixelArea().divide(1e6).rename('area_km2')
  .addBands(gfsm.rename('class'));

var grouped = areaImage.updateMask(validMask).reduceRegion({
  reducer: ee.Reducer.sum().group({
    groupField: 1,
    groupName: 'class'
  }),
  geometry: aoi,
  scale: 30,
  maxPixels: 1e13,
  tileScale: 4
});

var groups = ee.List(grouped.get('groups'));
var areaLookup = ee.Dictionary(groups.iterate(function(item, accumulator) {
  item = ee.Dictionary(item);
  accumulator = ee.Dictionary(accumulator);
  return accumulator.set(ee.Number(item.get('class')).format(), item.get('sum'));
}, ee.Dictionary({})));

var table = ee.FeatureCollection(classes.map(function(classValue) {
  classValue = ee.Number(classValue);
  var area = ee.Number(areaLookup.get(classValue.format(), 0));
  return ee.Feature(null, {
    class: classValue,
    area_km2: area
  });
}));

print('GFSM area by class, square kilometers', table);
Map.centerObject(aoi, 8);
Map.addLayer(gfsm.clip(aoi).updateMask(validMask), {
  min: 1,
  max: 5,
  palette: ['2c7bb6', 'abd9e9', 'ffffbf', 'fdae61', 'd7191c']
}, 'GFSM v1');
