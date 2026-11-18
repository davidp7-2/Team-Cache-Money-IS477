# Data Cleaning Documentation

## Dataset 1: Hospital General Information

**Source:** Centers for Medicare & Medicaid Services (CMS)

**Dataset:** Hospital General Information

**Source URL:** https://data.cms.gov/provider-data/dataset/xubh-q36u

### 1. Overview

The Hospital General Information dataset contains 5,419 hospital records. Before integration with he HCAHPS Patient Survey and Complications & Deaths datasets, we assessed the quality of the data using OpenRefine.

The dataset was generally consistent and well-structured, requiring minimal cleaning. In addition to addressing missing values and data types, we removed 29 unnecessary columns and retained nine columns relevant to our research question and integration process.

### 2. Data Quality Findings

| Column | Findings |
|---|---|
| Facility ID | 5,419 unique six-character IDs; no missing values |
| Hospital Overall Rating | 2,245 missing (41.4%); 3,174 valid |
| State | 56 geographic categories, including U.S. territories |
| Hospital Type | 8 valid categories |
| Hospital Ownership | 12 valid categories |
| ZIP Code | All 5,419 values contain exactly 5 digits |
| Core Identification Fields | No missing values | 

### 3. Cleaning Operations

**Operation 1: Standardize Missing Ratings**

Replaced "Not Available" in the Hospital Overall Rating column with null values.

GREL expression: if(value == "Not Available", null, value)

This standardized missing values without removing any hospital records.

**Operation 2: Convert Ratings to a Numeric format**

Converted valid Hospital Overall Rating values from strings to numeric values using OpenRefine's To number transformation.

All available ratings remained within the expected range of 1-5.

**Operation 3: Remove Unnecessary Columns**

The original dataset contained 38 columns. Using OpenRefine, we removed 29 columns that were not necessary for our planned integration and analysis.

The following nine columns were retained:
- Facility ID
- Facility Name
- Address
- City/Town
- State
- ZIP Code
- Hospital Type
- Hospital Ownership
- Hospital Overall Rating

These columns provide the hospital identifiers, geographic information, and hospital characteristics needed for our research. Facility ID will serve as the primary linkage attribute when integrating the three CMS datasets.

All 5,419 hospital records were preserved during this process.

### 4. Additional Validation

- Confirmed that Facility IDs remained six-character strings with leading zeros preserved.
- Reviewed state abbreviations, including territories, and identified no obvious inconsistencies.
- Reviewed all 8 Hospital Type categories and 12 Hospital Ownership categories.
- Verified that all ZIP codes matched a five-digit numeric format.

No additional transformations were necessary based on these checks.

### 5. Missing Data Decisions

All 5,419 hospital records were retained, including the 2,245 hospitals without an available overall rating. Missing ratings were not imputed because doing so would introduce unsupported values. The effect of missing ratings will be considered during analysis.

### 6. Reproducibility

The JSON recipe includes the transformations applied to Hospital Overall Rating and the removal of unnecessary columns, allowing the cleaned nine-column dataset to be reproduced from the original 38-column dataset.

**Files:**

- Original: data/raw/Hospital_General_Information.csv
- Cleaned: data/csv/Hospital-General-Information-Cleaned.csv
- OpenRefine recipe: openrefine/hospital_general_cleaning.json

To reproduce the cleaning, import the original CSV into OpenRefine, apply the operations from the JSON recipe using Undo / Redo -> Apply, and export the result as a CSV. The original dataset is preserved unchanged.


## Dataset 2: HCAHPS Patient Survey

**Source:** Centers for Medicare & Medicaid Services (CMS)

**Dataset:** HCAHPS Patient Survey

**Source URL:** https://data.cms.gov/provider-data/dataset/dgck-syfz

### 1. Overview

The original HCAHPS Patient Survey file contains 512,209 records and 22 columns. Most rows report the percentage of patients giving each answer to each question. Our research questions need one summary score per hospital per measure, so cleaning happened in two steps:

1. **Reduction (Python):** scripts/preprocessing/reduce_hcahps_data.py reads the original CMS zip and keeps only the 52,657 linear mean score rows and 11 relevant columns. Values are copied unchanged. This step is scripted rather than done by hand because the full file (about 173 MB) is too large to store uncompressed on GitHub, and a script makes the subset reproducible.
2. **Cleaning (OpenRefine):** the reduced file was cleaned in OpenRefine using the operations below.

All 52,657 records and all 4,787 hospitals were preserved.

### 2. Data Quality Findings

| Column | Findings |
|---|---|
| Facility ID | 4,787 unique six-character IDs; 164 end in "F", so IDs must stay as strings; no missing values |
| HCAHPS Measure ID | 11 linear-score measures; every hospital has all 11; no duplicate hospital/measure pairs |
| HCAHPS Linear Mean Value | 17,666 "Not Available" (33.5%); available values are whole numbers from 58 to 100 |
| Number of Completed Surveys | "Not Available" for 847 hospitals; available values range from 25 to 11,368 |
| Number of Completed Surveys Footnote | Present on every row with a missing score; explains why the score is missing |
| Patient Survey Star Rating | "Not Applicable" on all 52,657 rows |
| Start Date / End Date | One reporting period (01/01/2025 to 12/31/2025) stored as MM/DD/YYYY text |
| Text columns | No leading or trailing whitespace found |

### 3. Cleaning Operations

**Operation 1: Standardize Missing Scores**

Replaced "Not Available" in HCAHPS Linear Mean Value with null values.

GREL expression: if(value == "Not Available", null, value)

This prevents the text placeholder from being read as a value and keeps all hospital records.

**Operation 2: Convert Scores to a Numeric Format**

Converted HCAHPS Linear Mean Value from strings to numbers using value.toNumber(). All available scores stayed within the expected 0-100 range.

**Operation 3: Standardize Missing Survey Counts**

Applied the same two steps to Number of Completed Surveys: "Not Available" became null, and the remaining values were converted to numbers. Survey counts can be used later to flag or weight scores from hospitals with few responses.

**Operation 4: Standardize Dates**

Converted Start Date and End Date from MM/DD/YYYY text to ISO 8601 dates using value.toDate("MM/dd/yyyy"). This matches the date format used in the cleaned Complications and Deaths dataset, so reporting periods can be compared directly.

**Operation 5: Remove Uninformative Column**

Removed Patient Survey Star Rating because it is "Not Applicable" on every linear-score row and therefore contains no information.

The following ten columns were retained:
- Facility ID
- Facility Name
- State
- HCAHPS Measure ID
- HCAHPS Question
- HCAHPS Linear Mean Value
- Number of Completed Surveys
- Number of Completed Surveys Footnote
- Start Date
- End Date

### 4. Additional Validation

- Confirmed Facility IDs remained six-character strings, with leading zeros and "F" suffixes preserved.
- Confirmed there are no duplicate Facility ID and HCAHPS Measure ID combinations.
- Confirmed each HCAHPS Measure ID maps to exactly one HCAHPS Question.
- Checked all text columns for leading or trailing whitespace and found none, so no trimming was needed.

### 5. Missing Data Decisions

All 52,657 rows were kept, including the 1,606 hospitals with no available scores. Missing scores were not imputed: CMS suppresses these scores on purpose (the footnote codes give the reason), and filling them in would create unsupported values. The footnote column was kept so the reason for each missing value stays traceable. Hospitals without scores will be excluded from analyses that need HCAHPS values, and that exclusion will be documented.

### 6. Reproducibility

**Files:**

- Original: data/raw/HCAHPS_Patient_Survey.zip (checksum in data/raw/HCAHPS_Patient_Survey.sha256)
- Reduced (OpenRefine input): data/raw/HCAHPS_Patient_Survey_Reduced.csv
- Cleaned: data/csv/HCAHPS-Survey-Cleaned.csv
- OpenRefine recipe: openrefine/HCAHPS-Survey-Cleaning.json

To reproduce the cleaning:

1. Run python scripts/acquisitions/acquire_hcahps_data.py to verify the zip's SHA-256 checksum.
2. Run python scripts/preprocessing/reduce_hcahps_data.py to rebuild the reduced CSV.
3. Import data/raw/HCAHPS_Patient_Survey_Reduced.csv into OpenRefine with "Parse cell text into numbers, dates" turned off, so Facility IDs keep their leading zeros.
4. Apply openrefine/HCAHPS-Survey-Cleaning.json using Undo / Redo -> Apply, and export the result as CSV.

The original zip is preserved unchanged.

## Dataset 3: Hospital Complications and Deaths

**Source:** Centers for Medicare & Medicaid Services (CMS)

**Dataset:** Complications and Deaths – Hospital

**Dataset ID:** `ynj2-r877`

**Source URL:** https://data.cms.gov/provider-data/dataset/ynj2-r877

### 1. Overview

The Hospital Complications and Deaths dataset contains 95,740 records and 18 variables. It provides hospital-level quality measures related to complications, mortality, and patient outcomes.

Before integrating this dataset with Hospital General Information and the HCAHPS Patient Survey, we assessed its structure and data quality. Particular attention was given to Facility ID and Score because of their importance to the integration process and subsequent analysis.

### 2. Data Quality Findings

### 2. Data Quality Findings

| **Column** | **Findings** |
|---|---|
| Facility ID | Contains six-character hospital identifiers. Values repeat across records because individual hospitals have multiple reported quality measures. |
| Facility Name | Provides the corresponding hospital name for each record. |
| Address, City/Town, State, ZIP Code, County/Parish | Provide geographic information for identifying hospital locations. These fields were complete. |
| Telephone Number | Provides hospital contact information; no missing values identified. |
| Measure ID | Identifies the specific quality measure associated with each record. |
| Measure Name | Describes the complication, mortality, or other quality measure being reported. |
| Compared to National | Indicates how a hospital's performance compares with the national benchmark. |
| Denominator | Reports the number of cases used in calculating the corresponding measure. |
| Score | Approximately 46% of values were missing. Most available scores fell between 1 and 20, although many extended to 100 and one observation surpassed 100. |
| Lower Estimate, Higher Estimate | Provide the lower and upper estimates associated with the reported measure. |
| Footnote | Provides additional context or explanations for individual measure results. |
| Start Date, End Date | Identify the reporting period associated with each measure. Data extend through June 30, 2025. |

The repeated Facility IDs are expected because the dataset contains multiple measure-level records for individual hospitals. They do not indicate duplicate hospital records.

The repeated Facility IDs reflect the dataset's measure-level structure rather than duplicate hospital records.

### 3. Cleaning Operations

**Operation 1: Review Score Values**

Examined the Score distribution to identify unusual values and potential inconsistencies. Most observations fell between 1 and 20, although many extended to 100 and one exceeded 100. These values were evaluated in the context of their associated measures rather than automatically removed.

**Operation 2: Evaluate Missing Scores**

Reviewed missing Score values and distinguished unavailable results from actual numerical scores. Missing values or non-numeric entries were replaced will null values.

**Operation 3: Preserve Measure-Level Records**

Retained repeated Facility IDs because each record represents a potentially distinct quality measure. Removing these records would eliminate valid hospital-level information.

### 4. Additional Validation

- Reviewed all 18 variables and their roles in identifying hospitals and reported measures.
- Examined the Score distribution, including the observation exceeding 100.
- Reviewed the CMS definition of the Total Performance Score (TPS), which incorporates weighted quality domains.
- Confirmed that repeated Facility IDs were consistent with the dataset's measure-level structure.

### 5. Missing Data Decisions

Missing Score values were not imputed because unavailable results should not be interpreted as zero or assigned estimated performance values. These observations were retained, and the availability of scores will be considered when conducting comparisons and analysis.

### 6. Integration with Other CMS Datasets

Facility ID serves as the common linkage field across Hospital General Information, HCAHPS Patient Survey, and Hospital Complications and Deaths.

Hospital General Information contains one record for each of its 5,419 unique Facility IDs, while the Complications and Deaths dataset contains multiple measure-level records for individual hospitals. This creates a one-to-many relationship, allowing hospital characteristics to be associated with multiple quality measures while preserving the original measure-level information.

### 7. Reproducibility

The JSON recipe includes the transformations applied to Hospital Overall Rating and the removal of unnecessary columns, allowing the cleaned nine-column dataset to be reproduced from the original 38-column dataset.

**Files:**

- Original: data/raw/Complications_and_Deaths-Hospital.csv
- Cleaned: data/csv/Complications-Deaths-Cleaned.csv
- OpenRefine recipe: openrefine/Complications-Deaths-Cleaning.json

To reproduce the cleaning, import the original CSV into OpenRefine, apply the operations from the JSON recipe using Undo / Redo -> Apply, and export the result as a CSV. The original dataset is preserved unchanged.
