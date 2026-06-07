# FAQ

## Is GFSM a flood forecast?

No. GFSM is a flood susceptibility baseline. It does not forecast real-time floods and does not simulate event-specific inundation depth or extent.

## What do the five classes mean?

The five classes represent relative flood susceptibility: Very Low, Low, Moderate, High, and Very High. They are intended to support globally consistent screening and comparison.

## Where is GFSM in Google Earth Engine?

The public GFSM v1 ImageCollection is `projects/floodsus/assets/fsm_ei5`. It contains approximately 17,000 30 m tile images.

## Why are some pixels NoData?

NoData pixels may represent masked or unavailable areas, including open water, missing input coverage, or areas outside the modelled domain.

## Can I use GFSM for local planning?

GFSM can support screening and contextual analysis, but local planning should incorporate local observations, regulatory flood maps, flood defenses, drainage infrastructure, and engineering judgment.

## How should I calculate areas?

For quick summaries, use the provided Python or Earth Engine examples. For rigorous area estimates, reproject data to an appropriate equal-area CRS before calculating area.

## Does this repository include flood risk assessment?

No. Downstream flood risk assessment using exposure and vulnerability layers is outside the scope of this repository.
