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

### 4. Integration Strategy

The facility ID column will serve as the primary linkage key across all three datasets.

Hospital General Information provides hospital characteristics and supplemental quality information. HCAHPS will provide patient experience measures, while Complications & Deaths will provide clinical outcome measures.

The nine selected columns will be retained during integration, while the full cleaned Hospital General Information dataset will remain available separately.
