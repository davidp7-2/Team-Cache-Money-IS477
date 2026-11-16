# Pre-Integration Data Quality Assessment

## 1. Hospital General Information Dataset

Completeness: The Hospital General Information dataset contains 5,419 records. All nine hospital identification and descriptive variables assessed, including Facility ID, Facility Name, address, city/town, state, ZIP code, county/parish, hospital type, and hospital ownership, have no missing values. However, Hospital Overall rating is missing for 2,245 records (41.4%). Although this limits the usefulness of overall hospital ratings, the completeness of Facility ID supports integration with the other CMS datasets.

Accuracy: The Hospital General Information dataset was assessed for accuracy by examining Hospital Overall Rating values and Facility ID formatting. All Hospital Overall Rating values fall within the expected range of 1-5 or are marked as "Not Available," indicating that no invalid rating values were identified. Additionally, all Facility IDs follow the expected six-character format, with leading zeros preserved where applicable.

Since the dataset is published by the Centers for Medicare & Medicaid Services (CMS), it is considered a credible source of hospital information. However, the accuracy of individual hospital names, addresses, and reported rating was not independently verified against external sources. Therefore, while the assessed values appear valid, their accuracy cannot be fully confirmed without additional verification. 

Timeliness: The Hospital General Information dataset was last modified on October 26, 2026, so it is considered timely for the purposes of this project. However, this date reflects the dataset's modification rather than necessarily the reporting periods of the underlying hospital ratings. Additional examination of the reporting periods in the HCAHPS and Complications and Deaths datasets will be necessary to determine whether the datasets are compatible for integration.

Consistency: The Hospital General Information dataset was assessed for consistency by examining Facility IDs, state abbreviations, and other hospital identification variables. All Facility IDs follow a consistent six-character format, and no duplicate Facility IDs were identified among the 5,419 records. State values are consistently represented using two-letter abbreviations, and Hospital Overall Ratings follow a standardized scale of 1-5 or are marked as "Not Available."

Overall, no significant formatting inconsistencies or identification issues were found in the variables assessed. The hospital identification variables are complete and consistently formatted, suggesting that hospitals can be reliably identified within the dataset. Additionally, the uniqueness and consistent formatting of Facility IDs support their use as the primary key when integrating the three CMS datasets.
