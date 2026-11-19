# Data Integration Documentation

## Overview

The Hospital General Information, HCAHPS Patient Survey, and Complications and Deaths datasets were integrated to examine the relationship between hospital patient experience scores and clinical outcomes. All three datasets were obtained from the Centers for Medicare & Medicaid Services (CMS) and cleaned prior to integration.

The integration was performed using SQL through DuckDB in Python. Facility ID was used as the common joining attribute across all three datasets.

## Integration Method

The three datasets contained different numbers of records per hospital:

- **Hospital General Information:** 5,419 records, with one record per hospital.
- **HCAHPS Patient Survey:** 52,657 records, representing 11 patient experience measures for each of 4,787 hospitals.
- **Complications and Deaths:** 95,740 records, representing 20 clinical outcome measures for each of 4,787 hospitals.

Since HCAHPS and Complications and Deaths contained multiple records per hospital, directly joining the datasets would create unnecessary duplicated records.

To address this, SQL PIVOT operations were used to transform the HCAHPA and Complications and Deaths datasets into a wide format, where each measure could be a separate column.

The transformed datasets were then integrated with Hospital General Information using LEFT JOIN operations on Facility ID.

Hospital General Information served as the primary dataset, allowing all 5,419 hospital records to be preserved regardless of whether matching patient experience or clinical outcomes were available.

## Data Transformation and Missing Values

Facility IDs were preserved as text to maintain their original six-character format, including leading zeros and identifiers containing letters.

The HCAHPS Linear Mean Value and clinical outcome Score columns were converted to numeric values using SQL's TRY_CAST function. Values that could not be converted to numbers were represented as null.

Missing scores were not replaced or estimated, which is consistent with the decisions made during the initial data cleaning.

Individual patient experience and clinical outcome measures were preserved as separate columns because different measures represent different aspects of hospital performance.

The original cleaned datasets remain available and retain additional information such as measure descriptions, reporting periods, survey counts, and footnotes that were not included in the integrated analytical dataset.

## Integration Validation

The Integrated dataset was validated using SQL queries to check the number of records and unique hospital identifiers.

The following results were confirmed:

| Validation Metric | Result |
|---|---|
| Total hospital records | 5,419 |
| Unique Facility IDs | 5,419 |
| Duplicate Facility IDs | 0 |
| Total columns | 40 |
| Duplicate HCAHPS hospital-measure pairs | 0 |
| Duplicate clinical outcome hospital-measure pairs | 0 |

These results confirm that the integration preserved all hospitals from Hospital General Information without creating duplicate records.

## Limitations

Not all hospitals have available patient experience or clinical outcome scores. Missing values were retained to avoid introducing unsupported information.

Additionally, the datasets contain measures with different reporting periods, definitions, and scales. These differences will need to be considered when analyzing relationships between patient experience and clinical outcomes.

The integrated dataset can be used to examine associations between hospital characteristics, patient experience, and clinical outcomes, but the results cannot establish causation.

## Reproducibility

The integration was performed using a Python script containing DuckDB SQL queries. The script reads the three cleaned CSV files, performs the integration, validates the output, and exports the integrated dataset.

**Input files:** 

- `data/csv/Hospital-General-Information-Cleaned.csv`
- `data/csv/HCAHPS-Survey-Cleaned.csv`
- `data/csv/Complications-Deaths-Cleaned.csv`

**Integration script:**

- `scripts/integration/integrated_hospitals.csv`

**Output file:**

- `data/integrated/integrated_hospital.csv`

The script can be executed from the repository's root directory using:

`python scripts/integration/integrate_hospitals.py`

