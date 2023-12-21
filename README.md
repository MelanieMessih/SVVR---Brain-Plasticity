# Brain Plasticity

### Scientific Visualization & Virtual Reality - visualization project 
- University of Amsterdam
- November 2023 - December 2023

# REMOVE Molecular fingerprints --> REMOVE
In this study, 

an algorithm was developed that automatically calculates, selects, and combines molecular fingerprints from SMILES, and utilizes them to generate an optimized random forest regression model for the prediction of any target property.

### Requirements

This codebase is fully written in Python 3.9.13. The packages needed to sucessfully run the code are provided below:

```
import re, zipfile, os, pandas as pd, csv, numpy as np, matplotlib.pyplot as plt
from tqdm import tqdm
```

The following list describes the folder structure that can be found on this page.
- **Brain-Plasticity**: all of the files in this folder should be included in the main directory when running the code.
  - **/final_function.jl**: Julia file needed to generate the best fingerprint based on the given dataset. 
  - **/final_imports.jl**: Julia file with all imports needed.
  - **/final_functions.jl**: Julia file with all functions needed.
  - **/toxicity_data_fish.csv**: CSV fish toxicity data set used for this project.
  - **/descriptors.xml**: XML file needed to generate PaDEL fingerprints from SMILES.

- **code**: contains all functions needed to reproduce our work
  - **/brain_plasticity.py**: Python file including all functions

- **figures**: contains all figures that are created
  - **/no-network
  - **/disable
  - **/stimulus
  - **/calcium
 
- **

### Use

An example of how to run the function is provided below:

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
