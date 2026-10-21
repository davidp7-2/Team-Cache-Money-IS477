# Project Plan: Hospital Ratings, Patient Experience, and Clinical Outcomes

## 1. Overview

The goal of our project is to determine whether hospitals with higher patient experience ratings tend to have lower complication rates and mortality. We will use 3 datasets from the Centers for Medicare and Medicaid Services (CMS) that provide information about hospital ratings, patient experiences, and clinical outcomes.

We will start by exploring the datasets to understand their structure, identify relevant columns, and check for issues such as missing values and duplicate records. Next, we will clean and preprocess the data by standardizing column names and datatypes, and deciding how to handle missing or unavailable data. We will then combine the data using hospital facility identifiers and check that the resulting data is accurate.

Once we combine the datasets, we will use descriptive statistics, comparisons, and correlation analyses to help explain our findings. We will be looking specifically at relationships between patient experience scores, complication rates, and mortality. Finally, we will discuss the results and limitations of the data. As we received feedback throughout the project, we may adjust our approach to improve the analysis.


## 3. Research Questions

### Primary Research Question: 
Are hospitals with higher patient experience ratings associated with lower complication rates and mortality?
#### Supporting Questions:
Is there an association between hospital-level HCAHPS linear mean scores and selected complication measures?

Is there an association between hospital-level HCAHPS linear mean scores and selected 30-day mortality measures?

Do these relationships vary across different patient experience measures, such as nurse communication and doctor communication?

We will use descriptive statistics, visualizations, and other appropriate analyses to investigate these relationships. We will select clinical measures based on their definitions, availability, and how they compare across hospitals. Findings will be interpreted as associations rather than causation.

## 4. Datasets
### Dataset 1: Hospital General Information
Source: https://data.cms.gov/provider-data/dataset/xubh-q36u

This dataset contains general information about hospitals, including names, locations, facility identifiers, and star ratings. We will primarily use the facility identifier to connect hospitals across the datasets. The overall star rating mat be useful for additional context when examining hospital characteristics.

### Dataset 2: HCAHPS Patient Survey
Source: https://data.cms.gov/provider-data/dataset/dgck-syfz

This dataset contains information about patients' experiences with hospitals. It includes measures related to communication and aspects of care. We are using a reduced version of the original dataset that retains linear-score measures and selected columns relevant to the project. These scores will be used to compare patient experiences across various hospitals.

### Dataset 3: Complications an Deaths
Source: https://data.cms.gov/provider-data/dataset/ynj2-r877

This dataset contains hospital quality measures related to complications and mortality. We will examine the available measures and use the most appropriate ones for answering our research questions. These measures will be compared with patient experience scores to investigate whether hospitals with better reported patient experiences tend to have better clinical outcomes.

We plan to connect the datasets using hospital identifiers, which are expected to be labeled as Facility ID or something similar. We will verify the identifier column and ensure the data uses consistent formats. We will select or reorganize relevant measure before merging. After combining the datasets, we will check for unmatched hospitals, duplicate records, and any other outliers.
