"""Plot a local GFSM v1 GeoTIFF tile or clipped raster."""

from __future__ import annotations

import argparse

import matplotlib.colors as colors
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import rasterio


CLASS_NAMES = {
    1: "Very Low",
    2: "Low",
    3: "Moderate",
    4: "High",
    5: "Very High",
}
PALETTE = ["#2c7bb6", "#abd9e9", "#ffffbf", "#fdae61", "#d7191c"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("geotiff", help="Path to a GFSM GeoTIFF tile or clipped raster.")
    parser.add_argument(
        "--output",
        default="gfsm_tile.png",
        help="Output PNG path. Default: gfsm_tile.png",
    )
    parser.add_argument(
        "--title",
        default="GFSM v1 Flood Susceptibility",
        help="Plot title.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    with rasterio.open(args.geotiff) as src:
        data = src.read(1, masked=False)
        nodata = src.nodata if src.nodata is not None else 0
        masked = np.ma.masked_where(data == nodata, data)

    cmap = colors.ListedColormap(PALETTE)
    norm = colors.BoundaryNorm([1, 2, 3, 4, 5, 6], cmap.N)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(masked, cmap=cmap, norm=norm, interpolation="nearest")
    ax.set_title(args.title)
    ax.set_axis_off()

    legend_handles = [
        mpatches.Patch(color=PALETTE[value - 1], label=f"{value} - {name}")
        for value, name in CLASS_NAMES.items()
    ]
    ax.legend(handles=legend_handles, loc="lower left", frameon=True)

    fig.tight_layout()
    fig.savefig(args.output, dpi=200)
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
