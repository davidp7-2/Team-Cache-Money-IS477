# Data Cleaning Documentation

### Dataset 1: Hospital General Information

**Source:** Centers for Medicare & Medicaid Services (CMS)

**Dataset:** Hospital General Information

**Source URL:** https://data.cms.gov/provider-data/dataset/xubh-q36u

##### 1. Overview

The Hospital General Information dataset contains 5,419 hospital records. Before integration with he HCAHPS Patient Survey and Complications & Deaths datasets, we assessed the quality of the data using OpenRefine.

The dataset was generally consistent and well-structured, requiring minimal cleaning.

##### 2. Data Quality Findings

| Column | Findings |
|---|---|
| Facility ID | 5,419 unique six-character IDs; no missing values |
| Hospital Overall Rating | 2,245 missing (41.4%); 3,174 valid |
| State | 56 geographic categories, including U.S. territories |
| Hospital Type | 8 valid categories |
| Hospital Ownership | 12 valid categories |
| ZIP Code | All 5,419 values contain exactly 5 digits |
| Core Identification Fields | No missing values | 

##### 3. Cleaning Options

**Operation 1: Standardize Missing Ratings**

Replaced "Not Available" in the Hospital Overall Rating column with null values.

GREL expression: if(value == "Not Available", null, value)

This standardized missing values without removing any hospital records.

**Operation 2: Convert Ratings to a Numeric format**

Converted valid Hospital Overall Rating values from strings to numeric values using OpenRefine's To number transformation.

All available ratings remained within the expected range of 1-5.

##### 4. Additional Validation

- Confirmed that Facility IDs remained six-character strings with leading zeros preserved.
- Reviewed state abbreviations, including territories, and identified no obvious inconsistencies.
- Reviewed all 8 Hospital Type categories and 12 Hospital Ownership categories.
- Verified that all ZIP codes matched a five-digit numeric format.

No additional transformations were necessary based on these checks.

##### 5. Missing Data Decisions

All 5,419 hospital records were retained, including the 2,245 hospitals without an available overall rating. Missing ratings were not imputed because doing so would introduce unsupported values. The effect of missing ratings will be considered during analysis.

##### 6. Reproducibility

The cleaning operations were exported from OpenRefine as a JSON recipe.

**Files:**

- Original: data/raw/Hospital_General_Information.csv
- Cleaned: data/csv/hospital_general_cleaned.csv
- OpenRefine recipe: openrefine/hospital_general_cleaning.json

To reproduce the cleaning, import the original CSV into OpenRefine, apply the operations from the JSON recipe using Undo / Redo -> Apply, and export the result as a CSV. The original dataset is preserved unchanged.
