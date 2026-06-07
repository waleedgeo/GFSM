<div align="center">
  <a href="https://gfsm.waleedgeo.com">
    <img src="src/img/gfsm_logo_500px.png" alt="GFSM logo" width="150">
  </a>

  <h1>Global Flood Susceptibility Map (GFSM v1)</h1>

  <p>
    <strong>A globally harmonized 30 m flood susceptibility dataset built from multi-source Earth observation and geospatial data.</strong>
  </p>

  <p>
    <a href="https://gfsm.waleedgeo.com"><strong>Open GFSM Explorer</strong></a>
    ·
    <a href="https://doi.org/10.5281/zenodo.20568218"><strong>Zenodo DOI</strong></a>
    ·
    <a href="data_access/gee_quickstart.js"><strong>GEE quickstart</strong></a>
    ·
    <a href="examples/read_gfsm_tile_python.py"><strong>Python examples</strong></a>
  </p>

  <p>
    <a href="https://doi.org/10.5281/zenodo.20568218">
      <img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20568218-blue?style=flat-square&logo=zenodo" alt="Zenodo DOI">
    </a>
    <img src="https://img.shields.io/badge/Resolution-30%20m-2563eb?style=flat-square" alt="30 m resolution">
    <img src="https://img.shields.io/badge/Tiles-17%2C069-0f766e?style=flat-square" alt="17,069 tiles">
    <img src="https://img.shields.io/badge/GEE-ImageCollection-16a34a?style=flat-square&logo=googleearth" alt="Google Earth Engine ImageCollection">
    <img src="https://img.shields.io/badge/License-CC%20BY%204.0%20%2B%20MIT-6b7280?style=flat-square" alt="CC BY 4.0 and MIT license">
  </p>
</div>

---

<p align="center">
  <a href="https://gfsm.waleedgeo.com">
    <img src="src/img/gfsm_webapp.png" alt="GFSM Explorer application screenshot" width="100%">
  </a>
</p>

## What GFSM Provides

GFSM v1 maps relative flood susceptibility at 30 m resolution using five globally consistent classes. It is designed for dataset access, regional screening, visualization, clipping, and lightweight reproducible summaries.

This repository provides documentation, metadata, access instructions, compact validation metrics, Google Earth Engine scripts, Python examples, and minimal notebooks. Downstream flood-risk assessment with exposure and vulnerability layers is outside the scope of this repository.

## Access

| Resource | Identifier |
| --- | --- |
| Web app | https://gfsm.waleedgeo.com |
| Zenodo dataset DOI | https://doi.org/10.5281/zenodo.20568218 |
| Google Earth Engine asset | `projects/floodsus/assets/fsm_ei5` |

The Earth Engine asset is an `ImageCollection` containing approximately 17,000 GFSM 30 m tile images. The Zenodo record is the canonical dataset archive.

## At a Glance

| Attribute | GFSM v1 |
| --- | --- |
| Output product | Five-class EI-5 GeoTIFF tiles |
| Spatial resolution | 30 m |
| Spatial tiles | 17,069 processed global tiles |
| Modelling units | 192 country or country-climate units |
| Training samples | Approximately 30.45 million |
| Training label source | Aqueduct Flood Hazard Maps v2, 5-year baseline |
| Internal validation | Median ROC-AUC ~0.95; median AUPRC ~0.94 |
| DFO event correspondence | 79% within 5 km; 92% within 10 km |
| NoData | 0 = masked or unavailable |

## Class Legend

| Value | Class | Color |
| ---: | --- | --- |
| 0 | NoData / masked | <img src="https://img.shields.io/badge/NoData-d1d5db?style=flat-square&labelColor=d1d5db&color=d1d5db" alt="NoData color"> |
| 1 | Very Low | <img src="https://img.shields.io/badge/Very%20Low-2c7bb6?style=flat-square&labelColor=2c7bb6&color=2c7bb6" alt="Very Low color"> |
| 2 | Low | <img src="https://img.shields.io/badge/Low-abd9e9?style=flat-square&labelColor=abd9e9&color=abd9e9" alt="Low color"> |
| 3 | Moderate | <img src="https://img.shields.io/badge/Moderate-ffffbf?style=flat-square&labelColor=ffffbf&color=ffffbf" alt="Moderate color"> |
| 4 | High | <img src="https://img.shields.io/badge/High-fdae61?style=flat-square&labelColor=fdae61&color=fdae61" alt="High color"> |
| 5 | Very High | <img src="https://img.shields.io/badge/Very%20High-d7191c?style=flat-square&labelColor=d7191c&color=d7191c" alt="Very High color"> |

## Quickstart

### Google Earth Engine

```javascript
var gfsmCollection = ee.ImageCollection('projects/floodsus/assets/fsm_ei5');
var gfsm = gfsmCollection.mosaic().select(0).rename('gfsm');
var validMask = gfsm.gte(1).and(gfsm.lte(5));

var palette = ['2c7bb6', 'abd9e9', 'ffffbf', 'fdae61', 'd7191c'];
Map.addLayer(gfsm.updateMask(validMask), {min: 1, max: 5, palette: palette}, 'GFSM v1');
Map.setCenter(90.4, 23.7, 7);
```

More Earth Engine examples:

| Script | Purpose |
| --- | --- |
| [`gee_quickstart.js`](data_access/gee_quickstart.js) | Load and visualize GFSM |
| [`gee_visualize_gfsm.js`](data_access/gee_visualize_gfsm.js) | Add masked classes and a map legend |
| [`gee_clip_and_export.js`](data_access/gee_clip_and_export.js) | Clip GFSM to an AOI and export to Drive |
| [`gee_area_by_class.js`](data_access/gee_area_by_class.js) | Summarize area by susceptibility class |

### Python

```bash
pip install -r examples/requirements.txt
python examples/read_gfsm_tile_python.py path/to/GFSM_tile.tif
python examples/calculate_area_by_class_python.py path/to/GFSM_tile.tif --output area_by_class.csv
python examples/plot_gfsm_tile_python.py path/to/GFSM_tile.tif --output gfsm_tile.png
```

Python examples:

| Script | Purpose |
| --- | --- |
| [`read_gfsm_tile_python.py`](examples/read_gfsm_tile_python.py) | Print CRS, resolution, bounds, NoData, and class counts |
| [`calculate_area_by_class_python.py`](examples/calculate_area_by_class_python.py) | Calculate class areas from a tile or clipped raster |
| [`plot_gfsm_tile_python.py`](examples/plot_gfsm_tile_python.py) | Save a class-colored PNG |

## Repository Map

```text
GFSM/
├── data_access/          # Zenodo, tile-index, and Earth Engine examples
├── metadata/             # Class legend, tile schema, variables, scope
├── examples/             # Lightweight Python scripts
├── notebooks/            # Minimal local-tile notebooks
├── validation_summary/   # Manuscript-reported summary metrics
├── docs/                 # Citation, limitations, FAQ, changelog
├── src/img/              # Logo and app screenshot
├── CITATION.cff
├── LICENSE
└── README.md
```

## Scope Boundaries

Included:

- Dataset access and citation guidance.
- Google Earth Engine visualization, clipping, export, and class-area examples.
- Python examples for local GeoTIFF tiles.
- Class legend, tile schema, variable definitions, and compact validation summary.
- Responsible-use and limitation notes.

Not included:

- Exposure or vulnerability integration workflows.
- Population, asset, or infrastructure overlay analysis.
- Country rankings, hotspot rankings, damage estimates, or risk scores.
- Draft material for downstream GFSM-based flood-risk assessment studies.

## Validation Summary

The compact validation table in [`validation_summary/summary_metrics.csv`](validation_summary/summary_metrics.csv) reports the manuscript-level metrics intended for public reference. Internal ROC-AUC and AUPRC values describe discrimination against model-derived labels. DFO correspondence values provide independent event-based plausibility context.

## Responsible Use

GFSM is a susceptibility baseline, not a real-time flood forecast or event-specific inundation model. Use it for broad screening and comparative geospatial analysis, and combine it with local observations, flood-defense information, drainage infrastructure, engineering knowledge, and jurisdiction-specific planning guidance where possible.

See [`docs/known_limitations.md`](docs/known_limitations.md) and [`docs/faq.md`](docs/faq.md) for more detail.

## Citation

If you use GFSM v1, cite both the dataset DOI and the manuscript when available.

Dataset citation:

Waleed, M. (2026). Global Flood Susceptibility Map (GFSM v1): A high resolution (30m) flood susceptibility dataset derived from multi-source Earth observation and geospatial data [Data set]. Zenodo. https://doi.org/10.5281/zenodo.20568218

```bibtex
@dataset{waleed2026gfsm_data,
  author       = {Waleed, Mirza},
  title        = {{Global Flood Susceptibility Map (GFSM v1): A high resolution (30m) flood susceptibility dataset derived from multi-source Earth observation and geospatial data}},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {V1},
  doi          = {10.5281/zenodo.20568218},
  url          = {https://doi.org/10.5281/zenodo.20568218}
}
```

Manuscript citation placeholder:

```bibtex
@article{waleed2026gfsm,
  title   = {Global Flood Susceptibility Map (GFSM v1): A high resolution (30m) flood susceptibility dataset derived from multi-source Earth observation and geospatial data},
  author  = {Waleed, Mirza and Sajjad, Muhammad and Al-Ghamdi, Sami G. and Gao, Meng},
  journal = {Nature Scientific Data},
  year    = {2026},
  note    = {Manuscript under review}
}
```

Machine-readable citation metadata is provided in [`CITATION.cff`](CITATION.cff).

## Related Work

GFSM builds on recent flood susceptibility mapping and scalable GeoAI work:

- Waleed, M., & Sajjad, M. (2025). High-resolution flood susceptibility mapping and exposure assessment in Pakistan: An integrated artificial intelligence, machine learning and geospatial framework. *International Journal of Disaster Risk Reduction*, 121, 105442. https://doi.org/10.1016/j.ijdrr.2025.105442
- Waleed, M., & Sajjad, M. (2025). Advancing flood susceptibility prediction: A comparative assessment and scalability analysis of machine learning algorithms via artificial intelligence in high-risk regions of Pakistan. *Journal of Flood Risk Management*, 18(1), e13047. https://doi.org/10.1111/jfr3.13047

## License

Unless otherwise noted, GFSM data, metadata, and documentation are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). Code examples in this repository are licensed under the MIT License. See [`LICENSE`](LICENSE) for details.

## Project Contact

<div align="center">
  <h3>Mirza Waleed</h3>
  <p><strong>GeoAI, flood susceptibility mapping, and environmental risk research</strong></p>

  <p>
    <a href="https://waleedgeo.com">
      <img src="https://img.shields.io/badge/Website-waleedgeo.com-0f766e?style=flat-square" alt="Website">
    </a>
    <a href="mailto:waleedgeo@outlook.com">
      <img src="https://img.shields.io/badge/Email-waleedgeo%40outlook.com-2563eb?style=flat-square" alt="Email">
    </a>
    <a href="https://github.com/waleedgeo">
      <img src="https://img.shields.io/badge/GitHub-waleedgeo-111827?style=flat-square&logo=github" alt="GitHub">
    </a>
  </p>

  <p>
    For dataset access questions, citation updates, or GFSM web-app issues, use the contact links above.
  </p>
</div>
