<div align="center">
  <a href="https://waleedgis.users.earthengine.app/view/gfsm">
    <img src="src/img/gfsm_logo_500px.png" alt="GFSM Logo" width="180" height="180">
  </a>

  <h1 align="center">Global Flood Susceptibility Map (GFSM v1)</h1>
  <p align="center">
    <strong>A High-Resolution (30m) Global Dataset Derived from Multi-Source Geospatial Data</strong>
    <br />
    <br />
    <a href="https://waleedgis.users.earthengine.app/view/gfsm"><strong>Launch GEE App »</strong></a>
    <br />
    <br />
    <a href="#overview">Overview</a>
    ·
    <a href="#gfsm-explorer-app">Explorer App</a>
    ·
    <a href="#-dataset-access">Dataset Access</a>
    ·
    <a href="#-citation">Citation</a>
    ·
    <a href="#author--contact">Contact</a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Status-Under%20Review-orange?style=flat-square&logo=gitbook" alt="Status">
    <img src="https://img.shields.io/badge/Resolution-30m-blue?style=flat-square&logo=googleearth" alt="Resolution">
    <img src="https://img.shields.io/badge/Platform-Google%20Earth%20Engine-green?style=flat-square&logo=google" alt="GEE">
    <a href="https://doi.org/10.5281/zenodo.18137662">
      <img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18137662-blue?style=flat-square&logo=zenodo" alt="DOI">
    </a>
    <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
      <img src="https://img.shields.io/badge/License-CC%20BY--NC%20SA%204.0-lightgrey?style=flat-square&logo=creativecommons" alt="License">
    </a>
  </p>
</div>

<br />

## Overview

**GFSM v1** is the first globally harmonized flood susceptibility dataset produced at a native **30-meter spatial resolution**. Unlike traditional hazard models that rely on hydrodynamic simulations for specific return periods (e.g., 1-in-100 years), GFSM identifies the landscape's inherent propensity for flooding based on physical geographic and environmental controls.

Developed using a **Gradient-Boosted Tree (XGBoost)** machine learning framework, the model integrates topographic, hydrological, meteorological, and anthropogenic factors trained on over **30 million samples** across **192 distinct climate zones** and processed over **10,000 GB of high-resolution satellite data**.

### 🎯 Why GFSM?

- **First-of-its-kind:** Global harmonized susceptibility at 30m resolution
- **Data-rich foundation:** Trained on extensive multi-source geospatial datasets
- **Climate-aware:** Accounts for diverse climatic and geographic contexts
- **Actionable insights:** Suitable for regional planning, exposure assessment, and risk screening
- **Open science:** Data and methodology made available to the research community

> **📢 Project Status**
>
> The manuscript describing this dataset is currently **under review** at *Nature Scientific Data*. The dataset has been published on Zenodo (currently restricted) and will be made publicly available immediately following manuscript acceptance.
>
> **Dataset DOI:** [10.5281/zenodo.18137662](https://doi.org/10.5281/zenodo.18137662)

> 📧 For early access to specific tiles or training samples for validation purposes, please [contact the author](#author--contact) directly.

---

## GFSM Explorer App

Visualize and inspect the global dataset interactively using our Google Earth Engine web application. The app features smart-resolution switching and a click-to-inspect tool for detailed regional analytics.

<div align="center">
  <a href="https://gfsm.waleedgeo.com">
    <img src="src/img/gfsm_webapp.png" alt="GFSM App Interface" width="100%" style="border-radius: 10px; border: 1px solid #ddd;">
  </a>
</div>

> Click the image above to launch the app.

### Key App Capabilities:
* **Global Screening:** Rapidly visualize susceptibility patterns from global to local scales.
* **Resolution Toggling:** Switch between 1km overview layers and native 30m analysis layers.
* **Unit Inspector:** Click any location to view specific model performance metrics (AUC, F1-Score) for that region (coming soon).


---

## ✨ Key Features

### Coverage & Resolution
* 🌍 **Global Coverage:** Spans all inhabited landmasses from ~80°N to ~60°S
* 🎯 **High Precision:** Native 30m resolution for localized exposure assessment and infrastructure planning
* 📊 **Comprehensive Training:** Built on ~17,000 grid tiles across diverse geographic regions

### Technical Excellence
* 🤖 **Advanced ML Framework:** Gradient-Boosted Trees (XGBoost) optimized for geospatial prediction
* 🧪 **Robust Validation:** Global median AUC of **~0.95** across diverse terrains
* 🌐 **Climate-Aware:** Model trained across 192 distinct Köppen-Geiger climate zones

### Input Variables (9 Flood Conditioning Factors)

| Category | Variables | Data Source |
|----------|-----------|-------------|
| **Topographic** | Elevation, Slope, Aspect | FABDEM (30m) |
| **Hydrological** | HAND, TWI, Distance to Water | Derived from MERIT-Hydro |
| **Anthropogenic** | Distance to Roads, NDVI | OpenStreetMap, Sentinel-2 |
| **Climate** | Rainfall Frequency | GPM IMERG |

---

## Methodology

The generation of GFSM v1 followed a rigorous, high-performance computing workflow (involving distributed computing and advanced machine learning techniques on [SHAHEEN-III](https://www.kaust.edu.sa/en/research/shaheen) and [Google Earth Engine](https://earthengine.google.com/)). Details will be updated upon manuscript acceptance, but feel free to [reach out](#author--contact) for preliminary insights.

### Susceptibility Classes

| Class | Level | Description |
| :---: | :--- | :--- |
| **1** | **Very Low** | Areas with negligible flood propensity (e.g., high ridges, steep slopes). |
| **2** | **Low** | Areas with minimal risk factors. |
| **3** | **Moderate** | Transitional zones with some flood-prone characteristics. |
| **4** | **High** | Areas with significant flood conditioning factors. |
| **5** | **Very High** | Critical zones (floodplains, depressions) with maximum propensity. |

---

## 📂 Repository Structure

This repository serves as the official code and documentation hub for the GFSM project.

```text
GFSM/
├── scripts/              # Processing and analysis scripts (Coming soon)
│   ├── preprocessing/    # Data preparation workflows
│   ├── modeling/         # XGBoost training pipelines
│   └── inference/        # GEE-based prediction scripts
├── src/
│   ├── img/              # Visual assets (Logo, screenshots, diagrams)
│   └── docs/             # Additional documentation (Coming soon)
├── other/
│   └── sorting_zenodo/   # Utilities for dataset management
├── LICENSE               # CC BY-NC-SA 4.0 License
└── README.md             # Project documentation (this file)
```

> **Note:** Full processing scripts, training pipelines, and documentation will be released upon manuscript acceptance to ensure reproducibility.

---

## 📦 Dataset Access

The complete GFSM v1 dataset has been archived on Zenodo with a permanent DOI. The dataset is currently **restricted** and will be made **publicly available** immediately upon manuscript acceptance.

### Zenodo Repository

**Citation:** Waleed, M. (2026). Global Flood Susceptibility Map (GFSM v1): A high resolution (30m) flood susceptibility dataset derived from multi-source geospatial data (Version V1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.18137662

**DOI:** [10.5281/zenodo.18137662](https://doi.org/10.5281/zenodo.18137662)

### What's Included

The Zenodo archive contains:
- **Global GeoTIFF tiles** at 30m resolution
- **Metadata** and documentation for all layers
- **Global Tiles Index Grid** Allowing users to identify and download specific regions

### Access Methods

| Method | Status | Description |
|--------|--------|-------------|
| **Zenodo Direct Download** | 🔒 Restricted | Full dataset archive (Available post-publication) |
| **GEE Explorer App** | ✅ Live | Interactive visualization and inspection |
| **GEE Asset** | 🔜 Coming Soon | Programmatic access via Earth Engine API |
| **Early Access Request** | 📧 Available | Contact author for research purposes |

---

## 🗺️ Roadmap & Development Status

| Feature | Status | Timeline |
|---------|--------|----------|
| **GFSM Explorer (v1)** | ✅ Live | Available Now |
| **Zenodo Dataset Publication** | 🔒 Restricted | Published, opens upon acceptance |
| **Manuscript Publication** | 📝 Under Review | Submitted to *Nature Scientific Data* |
| **Public Dataset Download** | 🔜 Pending | Release upon acceptance |
| **GEE Asset (Public)** | 🔜 Pending | Release upon acceptance |
| **Processing Scripts** | 🔜 Pending | Release upon acceptance |
| **GFSM Toolbox (v2)** | 🚧 In Development | Q2 2026 (post-publication) |
| **API Integration** | 💡 Planned | Future Release |

> **Research Access:** Researchers requiring early access to specific tiles or training samples for validation purposes may [contact the author](#-author--contact) directly with reasonable request.

---

## 📖 Citation

If you use GFSM v1 in your research, please cite both the **manuscript** (upon publication) and the **dataset**.

### Primary Citation (Manuscript)

*Details to be updated upon publication*

```bibtex
@article{waleed2026gfsm,
  title={Global Flood Susceptibility Map (GFSM v1): A high resolution (30m) flood susceptibility dataset derived from multi-source geospatial data},
  author={Waleed, Mirza and Sajjad, Muhammad and Sami, Ghamdi and Meng, Gao},
  journal={Under Review at Nature Scientific Data},
  year={2026}
}
```

### Dataset Citation

```bibtex
@dataset{waleed2026gfsm_data,
  author       = {Waleed, Mirza},
  title        = {{Global Flood Susceptibility Map (GFSM v1): A high 
                   resolution (30m) flood susceptibility dataset derived 
                   from multi-source geospatial data}},
  month        = jan,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {V1},
  doi          = {10.5281/zenodo.18137662},
  url          = {https://doi.org/10.5281/zenodo.18137662}
}
```

### Related Publications

The methodology builds upon these foundational works:

- Waleed, M., & Sajjad, M. (2025). High-resolution flood susceptibility mapping and exposure assessment in Pakistan: An integrated artificial intelligence, machine learning and geospatial framework. *International Journal of Disaster Risk Reduction*, 121, 105442. https://doi.org/10.1016/j.ijdrr.2025.105442

- Waleed, M., & Sajjad, M. (2025). Advancing flood susceptibility prediction: A comparative assessment and scalability analysis of machine learning algorithms via artificial intelligence in high-risk regions of Pakistan. *Journal of Flood Risk Management*, 18(1), e13047. https://doi.org/10.1111/jfr3.13047

---

## Author & Contact
**Mirza Waleed**
<br />
*GeoAI & Environmental Risk Researcher*

* **Website:** [waleedgeo.com](https://waleedgeo.com)
* **Email:** [waleedgeo@outlook.com](mailto:waleedgeo@outlook.com)
* **LinkedIn:** [Mirza Waleed](https://www.linkedin.com/in/waleedgeo)
* **GitHub:** [@waleedgeo](https://github.com/waleedgeo)

Co-Authors: [Sajjad Muhammad](https://orcid.org/0000-0002-1576-1342) | [Sami G. Al-Ghamdi](https://orcid.org/0000-0002-7416-5153) | [Meng Gao](https://orcid.org/0000-0002-8657-3541)

---


## 🙏 Acknowledgments

This research was supported by:
- **Google Earth Engine** platform for massive-scale geospatial processing
- **SHAHEEN-III supercomputer** at KAUST for distributed computing resources
- Global open-access datasets: FABDEM, GPM IMERG, Sentinel-2, and others

We thank the reviewers and the scientific community for their valuable feedback.

---

## 📄 License

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.



<div align="left">
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>
</div>

Under this license, you are free to share and adapt the material, provided you give appropriate credit, do not use it for commercial purposes, and distribute any derivative works under the same license. For full license details, please visit the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons website</a>.