from pathlib import Path

# Point the `external` package to the vendored repo root so
# `external.generators.single_class` resolves correctly.
__path__ = [str(Path(__file__).resolve().parent / 'locality-concept-drift')]