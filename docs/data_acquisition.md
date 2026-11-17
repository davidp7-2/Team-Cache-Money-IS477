# Data Acquisition Documentation

## 1. Overview

Our project uses three datasets from the Centers for Medicare & Medicaid Services (CMS):
- Hospital General Information
- HCAHPS Patient Survey
- Complications & Deaths

We acquire the datasets programmatically to support transparency, data integration, and reproducibility.

This document currently describes acquisition of the Hospital General Information dataset. **Acquisition details for the remaining datasets will be added as their scripts are completed.**

## 2. Hospital General Information

**Source:** Centers for Medicare & Medicaid Services (CMS)

**Dataset ID:** xubh-q36u

**Source URL:** https://data.cms.gov/provider-data/dataset/xubh-q36u

**Acquisition script:** scripts/acquisitions/acquire_hospital_data.py

**Downloaded file:** data/raw/Hospital_General_Information.csv

### Acquisition Process

1. The python script sends an HTTP request to retrieve the CMS dataset
2. The response is checked for HTTP errors
3. The downloaded data is saved as a CSV in data/raw/.
4. A SHA-256 hash is calculated to verify the file's integrity.
5. The original CSV is prepared without modification

### Integrity Verification

The SHA-256 checksum recorded for the acquired Hospital General Information dataset is:

f874f09fef895a1ccf5bb7392dcbb2be05c9860339261b093fe00f0c1b013480

The checksum can be used to verify that the downloaded file matches the version used in our project.

Since the CMS datasets may be updated, a newly downloaded version could have a different checksum. A mismatch should be investigated rather than automatically treated as corruption.

### 3. Reproducing Data Acquisition

From the root directory of the GitHub repository, run:

python scripts/acquisitions/acquire_hospital_data.py

The script retrieves the dataset and saves it to the specified location.

The script's hash-verification procedure should be reviewed if CMS publishes a newer version of the dataset.

### 4. Data Preservation

The original downloaded CSV is stored in data/raw/.

All data cleaning occurs separately, and cleaned data is exported into data/csv/.

This ensures the original source remains available for verification and reproduction.

