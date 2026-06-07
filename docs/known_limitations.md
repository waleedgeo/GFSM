# Known Limitations

GFSM v1 is a flood susceptibility baseline, not an event-specific inundation forecast or real-time flood warning product.

Key limitations:

- Training labels are model-derived from Aqueduct Flood Hazard Maps v2, not direct flood observations.
- Training labels are coarser than the final 30 m output.
- The map reflects baseline or present-condition susceptibility and does not directly model future climate or future land-use change.
- Local flood defenses, fine-scale drainage infrastructure, and local engineering conditions may not be fully represented.
- Equal-interval classes support global consistency but may not match all local risk perceptions.
- NoData or masked pixels may reflect open water, missing input coverage, or areas outside the modelled domain.
- Users should combine GFSM with local observations, local flood maps, hydrologic expertise, and planning standards where possible.
