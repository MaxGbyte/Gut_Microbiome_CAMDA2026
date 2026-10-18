# The Gut Microbiome Interaction Network Challenge
<p>This repository contains approach to solving interaction networks inside gut microbiome compositional data published as part of CAMDA Contest Challanges in 2026.</p>

# Main Goal
Find possible communities of co-occurring microbiome taxa and assess their association with disease status.

# Workflow
1. Divide data into two groups: healthy, unhealthy
2. Use SparCC to determine significant correlations between taxons in groups
3. Build graph using output from SparCC
4. Check if we can see differences in graph structure between groups
5. Check if there are any node communities (using networkx build in functions)
6. Create ML classification models for each community to check their connection to inless status

# Available Data
Datasets available at [CAMDA datasets](https://bipress.boku.ac.at/camda2026/datasets/) in "The Gut Microbiome Interaction Network Challenge" section.

# Repository contents
```text
Gut_Microbiome_CAMDA2026/
|
|--- data/
|    |--- metadata.tsv
|    |--- pathways_relative_abundance.txt
|    |--- camda_README.txt
|    |--- taxonomy_relative_abundance.txt
|
|--- plots/     #All PNG files generated during models training and validation
|
|--- scripts/
|    |--- main_pipeline.ipynb
|
|--- requirements.yml
|--- README.md
```
