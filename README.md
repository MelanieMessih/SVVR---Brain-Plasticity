# Brain Plasticity

### Scientific Visualization & Virtual Reality - visualization project 
- University of Amsterdam
- November 2023 - December 2023

# REMOVE Molecular fingerprints --> REMOVE
In this study, ...........................................................

### Requirements

This codebase is fully written in Python 3.9.13. The packages needed to sucessfully run the code are provided below:

```
import re, zipfile, os, pandas as pd, csv, numpy as np, matplotlib.pyplot as plt
from tqdm import tqdm
```

It is required that the unzipped brain plasticity data is included in the same directory as from where the code is run. The data was retrieved from IEEE SciVis Contest 2023: https://sciviscontest2023.github.io/data/ (accessed on 2023-12-22).

The following list describes the folder structure that can be found on this page.
- **Brain-Plasticity**: 
  - **code**: contains all functions needed to reproduce our work
    - **code/brain_plasticity.py**: Python file including all functions for data preprocessing and visualization
 
  - **processed-data**: contains the preprocessed data needed to generate the visualizations
    - **processed-data/connections/no-network**: contains
    - **processed-data/connections/disable**: contains 
    - **processed-data/connections/stimulus**: contains
    - **processed-data/connections/calcium**: contains
      
    - **processed-data/monitor-areas/no-network**: contains
    - **processed-data/monitor-areas/disable**: contains 
    - **processed-data/monitor-areas/stimulus**: contains
    - **processed-data/monitor-areas/calcium**: contains

  - **figures**: contains all figures that were created --------------> automatic directory generation for figures!!!
    - **figures/connections/no-network**: ParaView 
    - **figures/connections/disable**: ParaView
    - **figures/connections/stimulus**: ParaView
    - **figures/connections/calcium**: ParaView
      
    - **figures/monitor-areas/no-network**: Python Matplotlib plot
    - **figures/monitor-areas/disable**: Python Matplotlib plot
    - **figures/monitor-areas/stimulus**: Python Matplotlib plot
    - **figures/monitor-areas/calcium**: Python Matplotlib plot

### Use

An example of how to run the function is provided below: -------------> fix

```
include("final_function.jl")
create_best_fingerprint(fish_toxicity_data, y_data, 2, index_col_nr=1, inchikeys_col_nr=4)
```

### REMOVE Structure --> REMOVE

The following list describes the folder structure that will be created when the code is run:
- **/fingerprints**: contains all fingerprints that are generated
  - **/fingerprints/PaDEL**: all PaDEL fingerprints
  - **/fingerprints/RDKit**: all RDKit fingerprints
  - **/fingerprints/combined_fingerprints**: all combined fingerprints
  
- **/summaries**: contains all summaries with scores and results that are created
  - **/summaries/PaDEL**: all PaDEL summaries
  - **/summaries/RDKit**: all RDKit summaries
  - **/summaries/combined_fingerprints**: all summaries of the combined fingerprints

- **/models**: contains all models that are created
  - **/models/PaDEL**: all PaDEL models
  - **/models/RDKit**: all RDKit models
  - **/models/combined_fingerprints**: all models of the combined fingerprints

- **/figures**: contains all figures that are created
  - **/figures/PaDEL**: all PaDEL figures
  - **/figures/RDKit**: all RDKit figures
  - **/figures/combined_fingerprints**: all figures of the combined fingerprints

## Authors
- Melanie Messih (13362933)
- Mike Meulendijks (13289179)

## Examiner
- Dr. R.G. Belleman
