# Tile Index Usage

GFSM v1 is distributed as tiled GeoTIFF data. Use the tile index from the Zenodo archive to identify which tile files intersect a study area before downloading or processing data.

## Typical Steps

1. Load the tile index in a GIS or Python environment.
2. Load or draw your area of interest.
3. Select tile footprints that intersect the area of interest.
4. Download the matching tile archives from Zenodo.
5. Mosaic, clip, or analyze only the necessary tiles.

## Python Sketch

```python
import geopandas as gpd

tiles = gpd.read_file("path/to/gfsm_tile_index.gpkg")
aoi = gpd.read_file("path/to/aoi.geojson").to_crs(tiles.crs)
selected = tiles[tiles.intersects(aoi.unary_union)]
print(selected)
```

## Notes

- Keep tile index files outside the repository if they are large.
- Reproject the AOI to the tile index CRS before spatial selection.
- Use the tile index as a download and processing aid; class values are stored in the GFSM GeoTIFF tiles.
