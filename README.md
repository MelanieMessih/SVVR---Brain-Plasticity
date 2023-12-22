# Brain Plasticity

### Scientific Visualization & Virtual Reality - visualization project 
- University of Amsterdam
- November 2023 - December 2023 

# Scientific Visualization of Brain Plasticity under Varying Circumstances: A Study on the Effect of Learning and Lesions on the Neuronal Network of the Human Brain
Brain plasticity plays a crucial role in the functioning of the brain. To investigate these effects, brain simulations models can be used that mimic the plasticity of the brain under varying circumstances. In this study, we are investigating the effects of learning and lesions on specific areas of the brain with scientific visualization.

### Requirements

This codebase is fully written in Python 3.9.13. The packages needed to sucessfully run the code are provided below:

```
import re, zipfile, os, pandas as pd, csv, numpy as np, matplotlib.pyplot as plt
from tqdm import tqdm
```

The brain plasticity data set was retrieved from IEEE SciVis Contest 2023: https://sciviscontest2023.github.io/data/ (accessed on 2023-12-22). It is required that the unzipped data directory is included in the same directory as from where the code is run.

The following list describes the folder structure that can be found on this page.
- **Brain-Plasticity**: 
  - **code**: contains all functions needed to reproduce our work
    - **code/brain_plasticity.py**: Python file including all functions for data preprocessing and visualization
 
  - **processed-data**: contains the preprocessed data needed to generate the visualizations
    - **processed-data/connections/no-network**: contains 202 txt files, one for each incoming and outgoing signal per step in the no-network simulation, with the connected source and target areas and their positions.
    - **processed-data/connections/disable**: contains 202 txt files, one for each incoming and outgoing signal per step in the disable simulation, with the connected source and target areas and their positions.
    - **processed-data/connections/stimulus**: contains 202 txt files, one for each incoming and outgoing signal per step in the stimulus simulation, with the connected source and target areas and their positions.
    - **processed-data/connections/calcium**: contains 202 txt files, one for each incoming and outgoing signal per step in the calcium simulation, with the connected source and target areas and their positions.
      
    - **processed-data/monitor-areas/no-network**: contains 48 csv files, one for each brain area, with information (e.g. grown and connected axons/dendrites and the calcium levels) per step in the no-network simulation.
    - **processed-data/monitor-areas/disable**: contains 48 csv files, one for each brain area, with information (e.g. grown and connected axons/dendrites and the calcium levels) per step in the disable simulation.
    - **processed-data/monitor-areas/stimulus**: contains 48 csv files, one for each brain area, with information (e.g. grown and connected axons/dendrites and the calcium levels) per step in the stimulus simulation.
    - **processed-data/monitor-areas/calcium**: contains 48 csv files, one for each brain area, with information (e.g. grown and connected axons/dendrites and the calcium levels) per step in the calcium simulation.

  - **figures**: contains the figures that were created --------------> automatic directory generation for figures!!!
    - **figures/connections/no-network**: ParaView .............
    - **figures/connections/disable**: ParaView ..........
    - **figures/connections/stimulus**: ParaView ..........
    - **figures/connections/calcium**: ParaView .............
      
    - **figures/monitor-areas/no-network**: contains 48 png figures, one for each brain area, with the grown and connected axons/dendrites and the calcium levels in the no-network simulations.
    - **figures/monitor-areas/disable**: contains 48 png figures, one for each brain area, with the grown and connected axons/dendrites and the calcium levels in the disable simulations.
    - **figures/monitor-areas/stimulus**: contains 48 png figures, one for each brain area, with the grown and connected axons/dendrites and the calcium levels in the stimulus simulations.
    - **figures/monitor-areas/calcium**: contains 48 png figures, one for each brain area, with the grown and connected axons/dendrites and the calcium levels in the calcium simulations.

### Use

The different functions from our workflow can be activated by uncommenting the function calls in the brain_plasticity.py file. These can be found under 'example usage' in the Python file. The selected functions can subsequently be called as follows:

```
python brain_plasticity.py
```

### Structure

The following list describes the folder structure that will be generated when the full code is run:
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
