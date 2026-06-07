# GFSM Tile Schema

GFSM v1 is distributed as 30 m five-class GeoTIFF tiles.

The public Google Earth Engine mirror is available as the ImageCollection `projects/floodsus/assets/fsm_ei5`, containing approximately 17,000 tile images.

## Tile Naming

The Zenodo archive uses GFSM tile package names such as `GFSM_N20W020.zip`. Individual raster tiles may use latitude-longitude tile IDs such as `N20W020` or similar coordinate-based names. Confirm the exact filename and footprint against the released Zenodo tile index.

## Raster Schema

| Field | Description |
| --- | --- |
| Format | GeoTIFF |
| Resolution | 30 m nominal output resolution |
| Data type | Integer class raster, typically byte-compatible values |
| NoData | 0 |
| Valid classes | 1, 2, 3, 4, 5 |
| Class meaning | Very Low, Low, Moderate, High, Very High flood susceptibility |
| CRS | Inspect per-tile metadata; use equal-area reprojection for rigorous area estimates |

## Coverage Notes

GFSM v1 is designed for near-global land coverage. Masked areas may include open water, areas outside model coverage, or pixels with insufficient input coverage. Always inspect tile metadata, NoData masks, and study-area coverage before analysis.

## Tile Index

Use the tile index from the Zenodo archive to find tile footprints that intersect a study region. See `data_access/tile_index_usage.md` for a lightweight usage example.
