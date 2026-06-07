"""Read a local GFSM v1 GeoTIFF tile and print basic metadata."""

from __future__ import annotations

import argparse

import numpy as np
import rasterio


CLASS_NAMES = {
    0: "NoData / masked",
    1: "Very Low",
    2: "Low",
    3: "Moderate",
    4: "High",
    5: "Very High",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("geotiff", help="Path to a GFSM GeoTIFF tile or clipped raster.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    with rasterio.open(args.geotiff) as src:
        data = src.read(1, masked=False)
        values, counts = np.unique(data, return_counts=True)

        print(f"File: {args.geotiff}")
        print(f"CRS: {src.crs}")
        print(f"Resolution: {src.res}")
        print(f"Bounds: {src.bounds}")
        print(f"Shape: {src.height} rows x {src.width} columns")
        print(f"NoData value: {src.nodata}")
        print("Class counts:")

        for value, count in zip(values.tolist(), counts.tolist()):
            label = CLASS_NAMES.get(int(value), "Unrecognized")
            print(f"  {int(value)} ({label}): {count}")


if __name__ == "__main__":
    main()
