# Milestone 3: Interim Status Report

## Overview

Our project examines whether hospitals with higher patient experience scores tend to have lower complication and mortality rates. We are using three datasets from the Centers for Medicare & Medicaid Services (CMS): Hospital General Information, HCAHPS Patient Survey, and Complications and Deaths.

Our goal is to integrate these datasets using hospital identifiers and analyze relationships between patient experiences and clinical outcomes. The project follows the data lifecycles discussed during class, specifically planning, data acquisition, data processing, analysis, preservation, and publication.

Since submitting our original project plan, we have made significant progress in preparing and integrating the datasets. We have organized our GitHub repository, documented data quality and cleaning decisions, and created an integrated dataset containing 5,419 unique hospitals. Our remaining priorities include conducting the analysis, implementing a Snakemake workflow, and testing the reproducibility of our project.

The original project scope and responsibilities are documented in `ProjectPlan.md`.

## Progress on Project Tasks

### Project Planning - Completed

Our first task was to establish the research question, identify datasets, assign team responsibilities, and organize the repository.

We selected three publicly available CMS datasets that contain hospital characteristics, patient experience scores, and clinical outcomes. We also established a timeline identifying major project milestone and assigned responsibilities among team members.

Our repository is organized into directories separating raw data, cleaned data, scripts, OpenRefine recipes, and documentation. This structure helps us track the transformations made throughout the data lifecycle while preserving the original datasets.

The organization strategy is described in `storage_organization.md`

### Data Exploration - Completed

Our next task involved examining the structure, variables, data types, and record counts of the three datasets to determine their suitability for integration.

Hospital General Information contained 5,419 hospital records and 38 original columns. We identified nine columns relevant to hospital identification, characteristics, and ratings.

The original HCAHPS dataset contained 512,209 records and 22 columns. Since many records represented response percentages that were unnecessary for our research question, we reduced the dataset to 52,657 linear mean score records.

The Complications and Deaths dataset contained 95,740 records and 18 columns. We identified clinical outcome scores, measure identifiers, reporting periods, and hospital identifiers as relevant variables.

An important discovery was the HCAHPS and Complications and Deaths contain multiple records per hospital, unlike Hospital General Information. This influenced our integration strategy.

Relevant variable definitions and dataset characteristics are documented in `data_dictionary.md`.

### Data Quality Assessment - Completed

We assessed the datasets using four data quality dimensions discussed in class: accuracy, completeness, timeliness, and consistency.

The Hospital General Information dataset contained 5,419 unique Facility IDs with no missing identifiers. However, 2,245 hospitals (41.4%) lacked an available overall rating.

The HCAHPS dataset contained 4,787 hospitals with 11 measures each. Approximately 33.5% of linear mean scores were unavailable. We also identified hospitals with suppressed scores and examined the corresponding CMS footnotes.

The Complications and Deaths dataset contained approximately 46% of missing scores. We examined its score distributions, repeated hospital identifiers, reporting periods, and consistency of descriptive variables.

We also verified that Facility ID was the most appropriate integration key. Some hospitals had different names between dataset, but their identifiers were consistent.

These findings are documented in `data_quality_assessment.md`

### Data Cleaning - Completed

After identifying data quality issues, we cleaned the three datasets using OpenRefine and Python.

For Hospital General Information, we standardized unavailable ratings as null values, converted valid rating to numbers, and removed 29 unnecessary columns. All 5,419 hospital records were retained.

For HCAHPS, we used a Python preprocessing script to reduce the original dataset before cleaning. We standardized missing values, converted linear mean scores and survey counts to numeric formats, converted reporting dates, and removed an uninformative column.

For Complications and Deaths, we reviewed unusual scores, standardized unavailable or nonnumeric scores as null values, and preserved the multiple measure-level records associated with each hospital.

We intentionally avoided imputing missing scores because if we did so we could introduce unsupported information. We also preserved the original datasets and stored OpenRefine JSON recipes to document the cleaning operations.

Our methods are described in `data_cleaning.md`, with the cleaned datasets stored in `data/csv/` and cleaning recipes in `openrefine/`.

### Data Integration - Completed and Validated

We integrated the three cleaned datasets using SQL through DuckDB in Python. 

Facility ID served as the common joining attribute. Since HCAHPS contained 11 measures per hospital and Complications contained 20 measures per hospital, directly joining the datasets would create unneeded duplicate records.

To address this, we used SQL PIVOT operations to transform the measure-level datasets into a format with one row per hospital. We then used LEFT JOIN operations to combine them with Hospital General Information.

We preserved all 5,419 hospitals from the primary dataset, including hospitals without matching survey clinical outcome information. Missing numeric scores remained null.

We validated the integrated dataset and confirmed that it contains 5,419 records, 40 columns, 5,419 unique facility IDs, and zero duplicate records. We also confirmed that neither measure-level dataset contained duplicate records.

The integration methodology and validation results are documented in `data_integration.md`.

The integration was tested using a standalone Python script, `scripts/integration/integrate_hospital.py`. The resulting dataset is saved as `data/integrated/integrated_hospital.csv`.

### Analysis and Visualization - In Progress

Our next task is to analyze the integrated dataset to determine whether patient experience scores are associated with complications and mortality measures.

We plan to use descriptive statistics, visualizations, and correlation analysis to examine relationships between HCAHPS scores and selected clinical outcome measures.

Particular attention will be given to patient experience measures such as nurse and doctor communication and relevant mortality measures.

Before conducting comparisons, we must determine which clinical measures are appropriate and account for missing values, different measurement scales, and reporting periods.

The analysis will focus on identifying associations rather than establishing causation. Results and visualizations will be documented and added to the repository.

### Workflow, Reproducibility, and Final Documentation - In Progress

Our final objective is to automate the project using Snakemake.

We have already separated data acquisition, preprocessing, and integration into Python scripts. We also documented cleaning transformations using OpenRefine recipes and organized the repository using relative file paths.

The next step is to create a Snakefile that connects these components into a reproducible workflow. We will also need to address how the OpenRefine cleaning steps can be reproduced automatically. 

After completing the workflow, we will test it from a fresh copy of the repository, document software dependencies, and verify that it produces the expected outputs.

## Updated Project Timeline

| Task | Original Deadline | Current Status | Expected Completion |
|---|---|--|---|
| Project Planning | 10/22 | Completed | Completed |
| Data Exploration | 10/29 | Completed | Completed|
| Data Quality Assessment | 11/5 | Completed | Completed |
| Data Cleaning and Integration | 11/12 | Completed | Completed |
| Analysis and Visualization | 11/19 | In Progress | Pushed back to 11/26 |
| Workflow and Documentation | 11/26 | In Progress | 11/26 |
| Reproducibility and Final Testing | 12/4 | Not yet completed | 12/4 |

## Changes to the Original Plan

Our overall research question and project scope have remained consistent with the original plan. However, we made a few adjustments as we learned more about the datasets.

First, we introduced a Python preprocessing step for the HCAHPS dataset because the original dataset was too large to manage in GitHub. This reduced the file size while retaining measures relevant to our analysis.

Second, we refined the integration strategy to account for differences in dataset granularity. Instead of directly joining the original measure-level datasets, we used SQL PIVOT operations to create a hospital-level dataset.

Third, we placed greater emphasis on documenting missing values and preserving original records. We retained hospitals with incomplete data rather than removing them before determining how useful they are for analysis.

These changes improved the organization and reproducibility of our project without changing our primary research objective.

## Challenges and Resolutions

### Large Dataset Size

The original HCAHPS dataset was too large for convenient storage and sharing in its uncompressed form.

We addressed this by retaining the original compressed dataset and developing a Python script to extract the relevant linear mean score records. This made the data more manageable while preserving a reproducible preparation process. 

### Missing and Unavailable Values

All three datasets contained missing or unavailable information, particularly hospital rating, HCAHPS scores, and clinical outcomes.

We standardized these values as nulls rather than estimating replacements. For future analysis, we will document how missing values affect the number of hospitals included in each comparison.

### Different Data Structures

Hospital General Information contained one record per hospital, while the other two datasets contained multiple measure-level records.

We resolved this by pivoting patient experience and clinical outcome measures into separate columns before joining the datasets. This presented unnecessary duplicate hospital records.

### Reporting Period Differences

The HCAHPS data cover January through December 2025, while clinical outcome measures use different reporting periods ending between March and June 2025.

These differences limit direct comparability. We will account for this when selecting measures and interpreting our results.

## Remaining Work and Next Steps

Our priority is to complete the analysis and visualization stage, including selecting appropriate clinical outcome measures and examining their relationships with patient experience scores.

Afterward, we will connect the processing scripts using Snakemake, finalize the data dictionary and documentation, and test the complete workflow for reproducibility.

We will also review our findings for limitations related to missing values, reporting periods, and differences among clinical measures.

Overall, we have completed the major data preparation and integration stages of the project. The remaining work will focus on interpreting the integrated data, automating our workflow, and ensuring another researcher can reproduce our results using the repository.

## Contributions

**David:** 
- Organized the repository
- Cleaned the Hospital General Information dataset while documenting the acquisition, data quality, data dictionary, and data cleaning along the way, to prepare the dataset for integration
- Created python scripts for acquisition and preprocessing of the Hospital General Information dataset
- Integrated the three datasets (python script) and documented the results and methodology
- Contributed to the creation of the Status Report

**John:**
- Cleaned the Hospital Complications and Deaths dataset while documenting the acquisition, data quality, data dictionary, and data cleaning along the way, to prepare the dataset for integration
- Created python scripts for acquisition and preprocessing of the Hospital Complications and Deaths dataset
- Contributed to the creation of the Status Report
**Eshan:**

**Elle:**
