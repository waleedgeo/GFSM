# Contributing to GFSM

Thank you for helping improve GFSM v1. Contributions that strengthen dataset access, documentation, metadata, examples, or reproducibility are welcome.

## Before Opening an Issue

- Check the [FAQ](docs/faq.md), [known limitations](docs/known_limitations.md), and existing GitHub issues.
- For a data problem, record the tile or region, class value, access route, and software used.
- For a documentation or code problem, include the file, command, observed behavior, and expected behavior.
- Do not attach large raster files. Share the smallest reproducible example or a link to the relevant Zenodo tile.

Questions involving unpublished downstream flood-risk analysis, private intermediate data, or unrelated workflows are outside this repository's scope.

## Proposing a Change

1. Fork the repository and create a focused branch.
2. Keep changes small and document any new dependency.
3. Preserve the GFSM class scheme (`0` = NoData; `1`-`5` = Very Low to Very High).
4. Run the affected example and check that linked paths still resolve.
5. Open a pull request explaining the problem, the change, and how it was verified.

By contributing, you agree that code contributions are licensed under the MIT License and documentation or metadata contributions are licensed under CC BY 4.0, as described in [LICENSE](LICENSE).
