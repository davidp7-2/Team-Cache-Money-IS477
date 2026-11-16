# Pre-Integration Data Quality Assessment

## 1. Hospital General Information Dataset

Completeness: The Hospital General Information dataset contains 5,419 records. All nine hospital identification and descriptive variables assessed, including Facility ID, Facility Name, address, city/town, state, ZIP code, county/parish, hospital type, and hospital ownership, have no missing values. However, Hospital Overall rating is missing for 2,245 records (41.4%). Although this limits the usefulness of overall hospital ratings, the completeness of Facility ID supports integration with the other CMS datasets.

Accuracy: The Hospital General Information dataset was assessed for accuracy by examining Hospital Overall Rating values and Facility ID formatting. All Hospital Overall Rating values fall within the expected range of 1-5 or are marked as "Not Available," indicating that no invalid rating values were identified. Additionally, all Facility IDs follow the expected six-character format, with leading zeros preserved where applicable.

Since the dataset is published by the Centers for Medicare & Medicaid Services (CMS), it is considered a credible source of hospital information. However, the accuracy of individual hospital names, addresses, and reported rating was not independently verified against external sources. Therefore, while the assessed values appear valid, their accuracy cannot be fully confirmed without additional verification. 
