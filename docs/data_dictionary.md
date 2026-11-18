# Data Dictionary

## 1. Overview

This data dictionary describes the variables selected for our IS 477 project, which examines whether higher hospital patient experiences scores are associated with lower complication and mortality rates.

Our project uses three datasets from the Centers for Medicare & Medicaid Services (CMS):
- Hospital General Information
- HCAHPS Patient Survey
- Complications & Deaths

The data dictionary will be expanded as we prepare the remaining datasets for integration.

## 2. Hospital General Information

**Source:** https://data.cms.gov/provider-data/dataset/xubh-q36u

**Original dataset:** 5,419 records and 38 columns.

**Cleaned dataset:** 5,419 records and 9 columns

**Unit of observation:** One hospital per Facility ID.

### Selected Variables

| Variable | Data Type | Description |
|---|---|---|
| Facility ID | String | Unique six-character hospital identifier used to integrate the three datasets |
| Facility Name | String | Name of hospital |
| Address | String | Street address of the hospital |
| City/Town | String | City or Town where the hospital is located |
| State | String | Two-character abbreviation identifying the state or US territory where the hospital is located |
| ZIP Code | String | Five-digit postal code identifying the hospital's location | 
| Hospital Type | String | CMS classification of the hospital, such as acute care or critical access |
| Hospital Ownership | String | Identifies the hospital's ownership category, such as government, nonprofit, or proprietary |
| Hospital overall rating | Numeric | Overall hospital ratings from 1-5. Unavailable ratings are represented as null |

### Data Quality Considerations

The Hospital General Information dataset was assessed and cleaned before integration.

- All 5,419 Facility IDs were unique and preserved as strings
- 2,245 hospitals (41.4%) had unavailable overall ratings
- All hospital records were retained
- State abbreviations and hospital classification categories were reviewed for consistency
- All ZIP Codes contain five digits and were preserved as strings
- The original 38 columns were reduced to nine relevant attributes.
- The original dataset was preserved without modification

## 3. HCAHPS Patient Survey

**Source:** https://data.cms.gov/provider-data/dataset/dgck-syfz

**Original dataset:** 512,209 records and 22 columns (data/raw/HCAHPS_Patient_Survey.zip)

**Reduced dataset:** 52,657 records and 11 columns (linear mean score rows only)

**Cleaned dataset:** 52,657 records and 10 columns (data/csv/HCAHPS-Survey-Cleaned.csv)

**Unit of observation:** One hospital per patient experience measure (long format; 11 rows per Facility ID).

**Reporting period:** January 1, 2025 to December 31, 2025

### Selected Variables

| Variable | Data Type | Description |
|---|---|---|
| Facility ID | String | Six-character CMS hospital identifier used to integrate the three datasets. Some IDs end in "F", so this must stay a string |
| Facility Name | String | Name of hospital as reported in the HCAHPS file |
| State | String | Two-character state or U.S. territory abbreviation |
| HCAHPS Measure ID | String | Code for the patient experience measure (see table below) |
| HCAHPS Question | String | Plain-language name of the measure |
| HCAHPS Linear Mean Value | Numeric | Hospital's linear mean score on a 0-100 scale; higher means a better patient experience. Null when CMS did not report a score |
| Number of Completed Surveys | Numeric | Number of HCAHPS surveys completed at the hospital during the reporting period. Null when not reported |
| Number of Completed Surveys Footnote | String | CMS footnote code(s) explaining missing or qualified values; blank when no footnote applies |
| Start Date | Date | Start of the reporting period (ISO 8601) |
| End Date | Date | End of the reporting period (ISO 8601) |

### HCAHPS Measures

| HCAHPS Measure ID | Measure |
|---|---|
| H_COMP_1_LINEAR_SCORE | Nurse communication |
| H_COMP_2_LINEAR_SCORE | Doctor communication |
| H_COMP_3_LINEAR_SCORE | Staff responsiveness |
| H_COMP_5_LINEAR_SCORE | Communication about medicines |
| H_COMP_6_LINEAR_SCORE | Discharge information |
| H_COMP_8_LINEAR_SCORE | Restfulness of environment |
| H_COMP_9_LINEAR_SCORE | Care coordination |
| H_CLEAN_LINEAR_SCORE | Cleanliness |
| H_SYMP_LINEAR_SCORE | Symptoms after stay |
| H_HSP_RATING_LINEAR_SCORE | Overall hospital rating |
| H_RECMND_LINEAR_SCORE | Recommend hospital |

### Data Quality Considerations

- 17,666 of 52,657 linear mean values (33.5%) are unavailable and stored as null
- Missingness is hospital-level: 3,181 hospitals have all 11 scores and 1,606 have none
- No duplicate Facility ID / Measure ID pairs
- Patient Survey Star Rating was removed because it is "Not Applicable" on every linear-score row
- The original zip is preserved without modification

### 4. Integration Strategy

The facility ID column will serve as the primary linkage key across all three datasets.

Hospital General Information provides hospital characteristics and supplemental quality information. HCAHPS will provide patient experience measures, while Complications & Deaths will provide clinical outcome measures.

The nine selected columns will be retained during integration, while the full cleaned Hospital General Information dataset will remain available separately.
