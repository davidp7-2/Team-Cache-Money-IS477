# Data Storage and Organization

## 1. Overview

Our project examines the relationship between hospital patient experience scores and clinical outcomes using three datasets from the Centers for Medicare & Medicaid Services (CMS):

- Hospital General Information
- HCAHPS Patient Survey
- Complication & Deaths

We organize our files in a GitHub repository to make our work accessible, understandable, and reproducible. We separate original datasets, cleaned datasets, scripts, and documentation so that each stage of the data lifecycle can be identified.

## 2. Repository Structure 

The repository is organized into the following directories:

| Directory | Purpose |
|---|---|
| data/raw/ | Stores original datasets downloaded from CMS |
| data/csv/ | Stores cleaned datasets prepared for integration |
| scripts/acquisitions/ | Contains scripts used to download datasets and verify integrity |
| openrefine/ | Stores OpenRefine JSON cleaning recipes |
| docs/ | Contains documentation describing data quality, cleaning, organization, and methodology |

**As the project progresses, additional scripts and folder will be used for data integration, analysis, and visualization.**

## 3. File Naming Conventions

We use descriptive filenames that identify the dataset and its purpose.

For example:
- Hospital_General_Information.csv - Original CMS dataset
- hospital_general_cleaned.csv - Cleaned Hospital General Information dataset
- acquire_hospital_data.py - Python script for downloading and verifying the dataset
- hospital_general_cleaning.json - OpenRefine cleaning operations

Python scripts use .py, datasets use .csv, cleaning recipes use .json, and documentation files use .md.

## 4. Raw and Processed Data

Original datasets are preserved in data/raw/ without modification.

Cleaning is performed on separate working copies, and cleaned datasets are exported into data/csv/.

This separation allows is to compare original and processed data, investigate changes, and reproduce our results without losing the original source information.

## 5. Reproducibility and Collaboration

GitHub is used to manage project files and track contributions from team members.

Each stage of the project is documented so that another researcher can understand how data moves from acquisition through cleaning, integration, and analysis.

We aim to use relative paths in our scripts so that the project can run on different computers without requiring changes to local directory paths.

The final project will include workflow automation, software dependencies, and instructions for reproducing the analysis.
