# Project Plan: Hospital Ratings, Patient Experience, and Clinical Outcomes

## 1. Overview

The goal of our project is to determine whether hospitals with higher patient experience ratings tend to have lower complication rates and mortality. We will use 3 datasets from the Centers for Medicare and Medicaid Services (CMS) that provide information about hospital ratings, patient experiences, and clinical outcomes.

We will start by exploring the datasets to understand their structure, usability, identify relevant columns, and check for issues such as missing values and duplicate records. Next, we will clean and preprocess the data by standardizing column names and datatypes, and deciding how to handle missing or unavailable data. We will then combine the data using hospital facility identifiers and assess the quality and accuracy of the data.

Once we combine the datasets, we will use descriptive statistics, comparisons, visualizations, and correlation analyses to help explain our findings. We will be looking specifically at relationships between patient experience scores, complication rates, and mortality. Finally, we will document our findings, data-cleaning decisions, and limitations. As we received feedback throughout the project, we may adjust our approach to improve the analysis.

The project will follow the data lifecycle stages that were discussed in class, from data acquisition and storage through processing, integration, analysis, and sharing. We will develop a reproducible workflow using separate scripts and an orchestrator so the analysis can be rerun from a fresh copy of the GitHub repository.

## 2. Team
### Team Member 1: David Podczerwinski
Help collect and organize the datasets and document their sources.

### Team Member 2: John Lewis
Explore the datasets and identify relevant variables.

### Team Member 3: Eshan Patel
Assist with the data-quality assessment and preprocessing.

### Team Member 4: Elle Crisostomo
Conduct the analysis, visualization, and interpretation.


## 3. Research Questions

### Primary Research Question: 
Is there an association between hospital patient experience scores and reported complication and mortality measures across U.S. hospitals?

#### Supporting Questions:
Do hospitals with higher HCAHPS patient experience scores tend to have lower complication rates?

Are hospitals with higher HCAHPS patient experience scores associated with lower mortality rates?

Is there an association between hospital-level HCAHPS linear mean scores and selected 30-day mortality measures?

Do these associations vary across different patient experience measures, such as nurse communication and doctor communication?

We will use descriptive statistics, visualizations, and other appropriate analyses to investigate these relationships. The specific measures and methods will depend on data availability, definitions, and techniques covered in class. We will interpret the findings as associations and not a direct causation. 

## 4. Datasets
### Dataset 1: Hospital General Information
Source: https://data.cms.gov/provider-data/dataset/xubh-q36u

This dataset contains general information about hospitals, including names, locations, facility identifiers, and star ratings. We will primarily use the facility identifier to connect hospitals across the datasets. The overall star rating may be useful for additional context when examining hospital characteristics.

### Dataset 2: HCAHPS Patient Survey
Source: https://data.cms.gov/provider-data/dataset/dgck-syfz

This dataset contains information about patients' experiences with hospitals. It includes measures related to communication and aspects of care. We are using a reduced version of the original dataset that retains linear-score measures and selected columns relevant to the project. These scores will be used to compare patient experiences across various hospitals.

### Dataset 3: Complications and Deaths
Source: https://data.cms.gov/provider-data/dataset/ynj2-r877

This dataset contains hospital quality measures related to complications and mortality. We will examine the available measures and use the most appropriate ones for answering our research questions. These measures will be compared with patient experience scores to investigate whether hospitals with better reported patient experiences tend to have better clinical outcomes.

We plan to connect the datasets using hospital identifiers, which are expected to be labeled as Facility ID or something similar. We will verify the identifier column and ensure the data uses consistent formats. As both the HCAHPS and Complications and Deaths datasets may contain multiple records per hospital, we will first need to filter or reshape the data to organize the specific measures before merging. The goal is to create a combined dataset with one row entry per hospital that includes separate columns for the selected patient experience and the clinical outcome measures. After combining the datasets, we will check for unmatched hospitals, duplicate records, and any other outliers.

## 5. Timeline

### Project Planning (Due 10/22) - David Podczerwinski

Finalize the research question, identify the datasets, assign responsibilities, and establish the project scope. Store the files and organize the repository. Determine the data lifecycle.

### Data Exploration (Due 10/29) - John Lewis

Inspect the datasets' file formats, data types, column names, record counts, and any other relevant measures. Document the data organization strategy and begin a data dictionary describing variables. 

### Data Quality Assessment (Due 11/5) - John Lewis + Eshan Patel

Assess each dataset for accuracy, completeness, timeliness, and consistency. Document the initial findings, investigate missing values and duplicates, and determine whether the datasets can be reasonably integrated.

### Data Cleaning and Integration (Due 11/12) - Eshan Patel

Clean the dataset as needed, including handling missing or suppressed values. Use Python/Pandas or SQL to integrate the dataset using hospital identifiers and document. Then, evaluate the integrated dataset for accuracy, completeness, timeliness, and consistency. Document the results, explaining whether the evidence supports successful integration.

### Analysis and Visualization (Due 11/19) - Elle Crisostomo

Conduct descriptive and statistical analyses to examine the relationships between patient experience scores and hospital complication and mortality measures. Create visualizations and document the methods, results, and limitations.

### Workflow and Documentation (Due 11/26) - David Podczerwinski

Organize the code into separate scripts and connect them to an orchestrator. Automate the workflow from data acquisition through analysis. Record data sources, processing decisions, and relevant information.

### Reproducibility and Final Testing/Reporting (Due 12/4) - Whole Group

Document the software requirements and package versions, using relative paths, and providing clear instructions for reproducing the results from a fresh repository. Complete the data dictionary and metadata documentation to support understanding and reuse of the datasets. Test the complete workflow, review the documentation and data quality assessments, and prepare the final report and project release.

## 6. Constraints

One of the first constraints we may encounter is hospitals having missing, unavailable, or suppressed values, which could affect our final analysis. 

The survey and clinical outcome datasets may contain multiple rows per hospital. This can create issues when combining the data. To resolve this, we will have to select or organize relevant measures before combining them. 

The measures used by hospitals may differ, as well as the reporting periods. We will need to review their definitions before comparing results.

The HCAHPS was too large to download into GitHub. Due to this, we uploaded a reduced subset from the original database that contained the measures and columns relevant to our research questions. We will document which measures and columns were retained and how this filtering occurred in a reproducible script that can retrieve and process the original data to generate the subset we are using. This will allow others to reproduce our preparation process without relying only on our modified file.

Large files, inconsistent hospital identifiers, and different dataset formats may complicate the cleaning and integration of datasets.

Patient experience and clinical outcomes may be related to other hospital characteristics not taken into consideration. Our analysis can only identify association, not causation.

## 7. Gaps

We will need to confirm the exact hospital identifier fields and verify they can be matched across all three datasets. 

Determine which complication and mortality rate measures are most appropriate to answer our research question.

Examine the datasets' reporting periods and determine whether they are comparable.

Decide how to deal with missing, suppressed, duplicate, and unmatched records after inspecting the data. 

Determine which statistical methods and visualizations are most appropriate for our analysis based on the data and techniques covered in class.

Decide how to organize the processing scripts and automate the workflow


