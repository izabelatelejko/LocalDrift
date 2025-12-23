# LocalDrift
Locality of Drift Research

## Real Datasets

| Dataset | Observations | Features | Classes |
|---------|--------------|----------|---------|
| Spam Corpus | 9,324 | 39,916 | 2 |
| Usenet1 | 1,500 | 99 | 2 |
| Usenet2 | 1,500 | 99 | 2 |
| Electricity | 45,312 | 8 | 2 |
| Weather | 18,159 | 8 | 2 |
| Airlines | 539,383 | 7 | 2 |
| Forest (Covertype) | 581,012 | 54 | 7 |
| Poker-Hand | 829,201 | 10 | 10 |


## Data sources

* Usenet1, Usenet2 - [An Ensemble of Classifiers for coping with Recurring Contexts in Data Streams](https://www.researchgate.net/publication/220836705_An_Ensemble_of_Classifiers_for_coping_with_Recurring_Contexts_in_Data_Streams)
* Spam Corpus (Gradual Concept Drift) - [Collected from Spam Assasin Corpus](http://mlkd.csd.auth.gr/datasets.html)
* Weather - [Incremental Learning of Concept Drift in Nonstationary Environments](http://users.rowan.edu/~polikar/research/nse/)
* Electricity (Abrupt) - [MOA - Normalized version](https://sourceforge.net/projects/moa-datastream/)
* Airlines (Abrupt) - [MOA](https://sourceforge.net/projects/moa-datastream/)
* Forest (Abrupt) - [MOA - Normalized version](https://sourceforge.net/projects/moa-datastream/)
* Poker-Hand - [MOA - Normalized version](https://sourceforge.net/projects/moa-datastream/)

## Syntehtic data

### Generators from `river` library

* Hyperplane - binary
* SEA - binary

### Generators from "A comprehensive analysis of concept drift locality in data streams"

Each stream can be genearted with __local__ or __global__ drift:

**RBF-based streams**: `emerging_cluster`, `reappearing_cluster`, `splitting_cluster`, `merging_cluster`, `moving_cluster`, `class_emerging_rbf`

**Tree-based streams**: `emerging_branch`, `prune_regrowth_branch`, `prune_growth_new_branch`, `class_emerging_rt`

## Methods

* CDLEEDS (Change Detection for Local Explainability in Evolving Data Streams) 

## External sources:

1. Project's Repository developed for "A comprehensive analysis of concept drift locality in data streams"

```
git subtree add --prefix=external/locality-concept-drift https://github.com/gabrieljaguiar/locality-concept-drift.git main --squash
```