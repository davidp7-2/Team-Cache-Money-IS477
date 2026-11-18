"""Reduce the full HCAHPS Patient Survey file to the rows and columns we use.

The full CMS file (about 173 MB uncompressed, 512,209 rows) is too large to
store uncompressed on GitHub, so the repository keeps the original zip and this
script rebuilds the reduced subset from it.

Input:  data/raw/HCAHPS_Patient_Survey.zip   (original CMS download)
Output: data/raw/HCAHPS_Patient_Survey_Reduced.csv  (input to OpenRefine)

Rows kept:    measures whose HCAHPS Measure ID ends in "_LINEAR_SCORE"
              (one 0-100 linear mean score per hospital per measure).
Columns kept: see KEEP_COLUMNS below. Values are copied unchanged.

Run from the repository root:
    python scripts/preprocessing/reduce_hcahps_data.py
"""
import csv
import io
import zipfile
from pathlib import Path

zip_path = Path("data/raw/HCAHPS_Patient_Survey.zip")
member_name = "HCAHPS Patient Survey.csv"
output_path = Path("data/raw/HCAHPS_Patient_Survey_Reduced.csv")

KEEP_COLUMNS = [
    "Facility ID",
    "Facility Name",
    "State",
    "HCAHPS Measure ID",
    "HCAHPS Question",
    "HCAHPS Linear Mean Value",
    "Patient Survey Star Rating",
    "Number of Completed Surveys",
    "Number of Completed Surveys Footnote",
    "Start Date",
    "End Date",
]

rows_read = 0
rows_kept = 0

with zipfile.ZipFile(zip_path) as archive:
    with archive.open(member_name) as raw_file:
        reader = csv.DictReader(io.TextIOWrapper(raw_file, encoding="utf-8", newline=""))
        with open(output_path, "w", encoding="utf-8", newline="") as out_file:
            writer = csv.writer(out_file, lineterminator="\r\n")
            writer.writerow(KEEP_COLUMNS)
            for row in reader:
                rows_read += 1
                if row["HCAHPS Measure ID"].endswith("_LINEAR_SCORE"):
                    writer.writerow([row[column] for column in KEEP_COLUMNS])
                    rows_kept += 1

print("Rows read from full file:", rows_read)
print("Linear-score rows kept:  ", rows_kept)
print("Columns kept:            ", len(KEEP_COLUMNS))
print("Reduced file written to: ", output_path)
