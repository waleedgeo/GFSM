# Download GFSM v1 from Zenodo

The canonical GFSM v1 dataset archive is hosted on Zenodo:

- DOI: https://doi.org/10.5281/zenodo.20568218
- Data product: GFSM v1
- Zenodo record version: v2
- Google Earth Engine mirror: `projects/floodsus/assets/fsm_ei5`

Use the Zenodo record to download the released GFSM GeoTIFF tile archives and accompanying metadata. The archive is expected to include global GeoTIFF tiles and a tile index that helps identify the files needed for a region of interest.

Recommended workflow:

1. Open the Zenodo record and review the current file list and release notes.
2. Download only the tile archive(s) needed for your study area when possible.
3. Verify downloaded archives before extracting.
4. Keep the raw downloaded files unchanged and run analyses from a separate working folder.
5. Cite the Zenodo DOI in derived products and publications.

Do not commit downloaded GeoTIFFs, compressed tile archives, shapefiles, or other large geospatial data into this GitHub repository.

## Location downloads in GFSM Explorer

The local GFSM Explorer source now supports a location download lookup. Once that source is published, clicking a location will use the released tile index to identify the regional ZIP that covers the clicked tile. It will show the tile ID, exact ZIP filename, and approximate ZIP size below the download link. ZIP sizes are rounded from the exact byte counts in the [v2 archive manifest](zenodo_v2_archives.csv). A regional ZIP contains many native 30 m tiles; the app's display-resolution selector does not change the downloaded files. Individual tile files are inside the ZIPs and are not offered as separate Zenodo downloads.

The app queries the Earth Engine table `projects/floodsus/assets/GFSM_Tile_Index_v1`. Its shapefile-derived fields `tile_id` and `zip_filena` correspond to the GeoPackage fields `tile_id` and `zip_filename`. The app accepts a ZIP name only if it appears in the v2 manifest, then links to that file on Zenodo record `20568218`. It shows all distinct archive matches at a boundary and keeps a quieter full-record link below the location inspector.

After a click, the map draws a cyan bounding outline around the indexed tiles in the selected ZIP. The rectangle's interior stays transparent: it shows the ZIP's tile extent, not continuous data coverage. If several ZIPs meet at the point, use the inspector's selector to change which ZIP area is shown. The Zoom button frames the shown ZIP area. A new click or Reset clears the overlay.

To refresh the manifest for this release, run `python data_access/build_zenodo_manifest.py` from the repository root. The script reads the Zenodo record API, checks every regional ZIP name against the local `GFSM_Tile_Index_v1.gpkg`, verifies the local index ZIP checksum when present, writes the CSV, and updates the generated size lookup in the local Earth Engine app source at `.unpublished/gee_gfsm_app_codes.js`. Pass `--record-json PATH` to use a saved API response. When changing releases, update the record ID and index asset deliberately and validate the new file list before publishing the app.
