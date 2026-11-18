# Data Acquisition Documentation

## 1. Overview

Our project uses three datasets from the Centers for Medicare & Medicaid Services (CMS):
- Hospital General Information
- HCAHPS Patient Survey
- Complications & Deaths

We acquire the datasets programmatically to support transparency, data integration, and reproducibility.

This document currently describes acquisition of the Hospital General Information and HCAHPS Patient Survey datasets. **Acquisition details for the remaining dataset will be added as its script is completed.**

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


## 5. HCAHPS Patient Survey

**Source:** Centers for Medicare & Medicaid Services (CMS)

**Dataset ID:** dgck-syfz

**Source URL:** https://data.cms.gov/provider-data/dataset/dgck-syfz

**Reporting period of the version used:** January 1, 2025 to December 31, 2025

**Downloaded file:** data/raw/HCAHPS_Patient_Survey.zip (11.5 MB; contains "HCAHPS Patient Survey.csv", 173 MB)

**Integrity script:** scripts/acquisitions/acquire_hcahps_data.py

**Reduction script:** scripts/preprocessing/reduce_hcahps_data.py

### Acquisition Process

1. The HCAHPS Patient Survey dataset was downloaded from the CMS Provider Data Catalog as a zip file and saved to data/raw/.
2. The zip is stored in the repository because it is under GitHub's 50 MB limit, while the uncompressed CSV is not.
3. The integrity script computes the zip's SHA-256 checksum and compares it with the expected value in data/raw/HCAHPS_Patient_Survey.sha256. It exits with an error if they do not match.
4. The reduction script reads the CSV directly from the zip and writes the 52,657 linear mean score rows to data/raw/HCAHPS_Patient_Survey_Reduced.csv, which is the input for OpenRefine cleaning.

### Integrity Verification

The SHA-256 checksum recorded for the acquired HCAHPS Patient Survey zip is:

e55d624ca61d652f476f7d718deaf55d72053f8c921bdc67c1a3d6516e40bbec

CMS replaces this dataset with each quarterly refresh, so a new download from the source URL will cover a different reporting period and have a different checksum. The committed zip is the version used in this project.

### Reproducing Data Acquisition

From the root directory of the GitHub repository, run:

python scripts/acquisitions/acquire_hcahps_data.py

python scripts/preprocessing/reduce_hcahps_data.py

Both scripts use only the Python standard library.

### Version Note

An earlier reduced file (patient_survey_reduced.csv, reporting period October 1, 2024 to September 30, 2025) was used during project planning. The original CMS file it was built from is no longer published, so it could not be regenerated. It was replaced by the version above, which keeps the original download in the repository and rebuilds the subset with a script.
