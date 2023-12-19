# SVVR-Brain-Plasticity

### Bachelor project 
- Bachelor programme: Chemistry (joint degree UvA/VU)
- Duration: 3 months (April 2023 - June 2023)

# Molecular fingerprints
In this study, an algorithm was developed that automatically calculates, selects, and combines molecular fingerprints from SMILES, and utilizes them to generate an optimized random forest regression model for the prediction of any target property.

### Requirements

This codebase is fully written in Julia 1.6.7. The packages needed to sucessfully run the code are provided below:

```
using Pkg, CSV, DataFrames, PyCall, Conda, ScikitLearn, Statistics, Plots, Tables, Plots.PlotMeasures, LightXML, LinearAlgebra, ProgressBars, OrderedCollections, Base.Filesystem
```

To calculate molecular fingerprints, Java needs to be installed (https://www.java.com/en/download/manual.jsp). Other packages needed are installed using Conda and pyimport from PyCall.

The following list describes the folder structure that can be found on this page.
- **Bachelorproject**: all of the files in this folder should be included in the main directory when running the code.
  - **/final_function.jl**: Julia file needed to generate the best fingerprint based on the given dataset. 
  - **/final_imports.jl**: Julia file with all imports needed.
  - **/final_functions.jl**: Julia file with all functions needed.
  - **/toxicity_data_fish.csv**: CSV fish toxicity data set used for this project.
  - **/descriptors.xml**: XML file needed to generate PaDEL fingerprints from SMILES.

### Use

An example of how to run the function is provided below:

```
include("final_function.jl")
create_best_fingerprint(fish_toxicity_data, y_data, 2, index_col_nr=1, inchikeys_col_nr=4)
```

### Overview functions

- Included in final_function.jl:
#### create_best_fingerprint(dataset, y_data, smiles_col_nr; index_col_nr=nothing, inchikeys_col_nr=nothing, limit_train_score=0.8, limit_test_score=0.5, variance_explained=85)
    This function takes a DataFrame of the dataset that contains columns with X data, SMILES and optionally indices 
    and inchikeys, a vector of y data, and the column number of the DataFrame that contains SMILES. Optional
    parameters are the column numbers that contain indices and inchikeys, two floats between 0 and 1 that represent 
    the minimum train and test score for the selection of the fingerprints, and an integer between 0 and 100 that 
    represents the variance percentage you want to have explained by the important features. 
    
    The function generates PaDEL and RDKit fingerprints, creates and optimizes random forest regressor models with 
    them, selects the fingerprints of which the train and test score exceed the given limit_train_score and 
    limit_test_score, and combines the selected fingerprints into one fingerprint. This final fingerprint is used to
    create the final random forest model, which is trained and optimized. 
    
    During this process, summaries of the scores and results, the generated fingerprints, and the generated figures 
    are saved as CSV files and the created models are saved as JOBLIB files. 
    
    Parameters:
    - dataset: DataFrame that at least contains columns with X data, y data and SMILES of chemicals. 
    - y_data: Vector with elements of type Int or Float.
    - smiles_col_nr=nothing: Int.
    - index_col_nr=nothing: Int.
    - limit_train_score=0.8: Float between 0 and 1.
    - limit_test_score=0.5: Float between 0 and 1. 
    - variance_explained=85: Int between 0 and 100. 

- Included in final_functions.jl:
#### remove_features(X_data, headers=[])
    This function takes a DataFrame or Matrix as input. When a DataFrame is given, "headers" can be left empty. When 
    a Matrix is given, headers should be spicified to make sure the column headers are known when working with the 
    data. The function removes columns with missing, nan or inf values and returns the cleaned up Dataframe or Matrix 
    and its headers. 
    
    Parameters:
    - X_data: DataFrame or Matrix.
    - headers=[]: if X_data is a Matrix, headers should be specified as a Vector with elements of type Str.
    
    Returns:
    - X_data: DataFrame or Matrix.
    - headers: Vector with elements of type Str.

### Structure

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
- Melanie Messih

## Supervisors
- Dr. Saer Samanipour
- Viktoriia Turkina MSc

## Research group, research institute and university
Environmental Modeling & Computational Mass Spectrometry (EMCMS), Analytical Chemistry Group, Van 't Hoff Institute for Molecular Sciences (HIMS), University of Amsterdam (UvA)

https://emcms.info/ 
