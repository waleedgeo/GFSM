"""Calculate area by GFSM v1 class for a local GeoTIFF tile or clipped raster."""

from __future__ import annotations

import argparse
import warnings

import numpy as np
import pandas as pd
import rasterio
from pyproj import CRS
from pyproj import Geod


CLASS_NAMES = {
    1: "Very Low",
    2: "Low",
    3: "Moderate",
    4: "High",
    5: "Very High",
}


def projected_pixel_area_km2(src: rasterio.io.DatasetReader) -> float:
    """Return one pixel area in square kilometers for a projected raster."""
    transform = src.transform
    area_in_crs_units = abs(transform.a * transform.e - transform.b * transform.d)

    x_factor = 1.0
    y_factor = 1.0
    if src.crs:
        pyproj_crs = CRS.from_user_input(src.crs)
        axis_info = pyproj_crs.axis_info
        if axis_info:
            x_factor = getattr(axis_info[0], "unit_conversion_factor", 1.0)
        if len(axis_info) > 1:
            y_factor = getattr(axis_info[1], "unit_conversion_factor", x_factor)
        else:
            y_factor = x_factor

    return area_in_crs_units * x_factor * y_factor / 1_000_000.0


def geodesic_area_by_class_km2(
    data: np.ndarray,
    transform: rasterio.Affine,
    nodata: int | float,
) -> dict[int, float]:
    """Calculate class areas on a north-up geographic grid using WGS84 geodesics."""
    if not np.isclose(transform.b, 0.0) or not np.isclose(transform.d, 0.0):
        raise ValueError(
            "Rotated geographic rasters are not supported by this lightweight example. "
            "Reproject to an equal-area CRS first."
        )

    geod = Geod(ellps="WGS84")
    areas = {class_value: 0.0 for class_value in CLASS_NAMES}

    for row in range(data.shape[0]):
        left, top = transform * (0, row)
        right, bottom = transform * (1, row + 1)
        pixel_area_m2, _ = geod.polygon_area_perimeter(
            [left, right, right, left],
            [top, top, bottom, bottom],
        )
        pixel_area_km2 = abs(pixel_area_m2) / 1_000_000.0

        row_values = data[row, :]
        for class_value in CLASS_NAMES:
            count = int(np.count_nonzero((row_values == class_value) & (row_values != nodata)))
            areas[class_value] += count * pixel_area_km2

    return areas


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("geotiff", help="Path to a GFSM GeoTIFF tile or clipped raster.")
    parser.add_argument(
        "--output",
        default="gfsm_area_by_class.csv",
        help="Output CSV path. Default: gfsm_area_by_class.csv",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    with rasterio.open(args.geotiff) as src:
        data = src.read(1, masked=False)
        nodata = src.nodata if src.nodata is not None else 0

        if src.crs and src.crs.is_geographic:
            warnings.warn(
                "The raster CRS is geographic. This example uses WGS84 geodesic "
                "pixel areas; for large production summaries, an appropriate "
                "equal-area reprojection is still recommended.",
                RuntimeWarning,
            )
            area_by_class = geodesic_area_by_class_km2(data, src.transform, nodata)
        else:
            if not src.crs:
                warnings.warn(
                    "The raster CRS is missing. Area is calculated from transform "
                    "units as if they are meters.",
                    RuntimeWarning,
                )
            pixel_area_km2 = projected_pixel_area_km2(src)
            area_by_class = {
                class_value: int(np.count_nonzero((data == class_value) & (data != nodata)))
                * pixel_area_km2
                for class_value in CLASS_NAMES
            }

        rows = []
        for class_value, class_name in CLASS_NAMES.items():
            pixel_count = int(np.count_nonzero((data == class_value) & (data != nodata)))
            rows.append(
                {
                    "value": class_value,
                    "class_name": class_name,
                    "pixel_count": pixel_count,
                    "area_km2": area_by_class[class_value],
                }
            )

    table = pd.DataFrame(rows)
    table.to_csv(args.output, index=False)
    print(table.to_string(index=False))
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
