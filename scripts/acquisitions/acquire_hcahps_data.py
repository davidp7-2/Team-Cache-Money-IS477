"""Verify the integrity of the HCAHPS Patient Survey download.

Computes the SHA-256 checksum of data/raw/HCAHPS_Patient_Survey.zip and
compares it with the expected value stored in
data/raw/HCAHPS_Patient_Survey.sha256. Exits with an error if they differ.

Run from the repository root:
    python scripts/acquisitions/acquire_hcahps_data.py
"""
import hashlib
import sys
from pathlib import Path

file_path = Path("data/raw/HCAHPS_Patient_Survey.zip")
checksum_path = Path("data/raw/HCAHPS_Patient_Survey.sha256")

sha256_hash = hashlib.sha256()
with open(file_path, "rb") as file:
    for chunk in iter(lambda: file.read(4096), b""):
        sha256_hash.update(chunk)

checksum = sha256_hash.hexdigest()
expected = checksum_path.read_text().split()[0].lower()

print("Dataset:", file_path.name)
print("SHA256 Checksum:", checksum)
print("Expected:       ", expected)

if checksum != expected:
    print("File integrity check FAILED: checksum does not match.")
    sys.exit(1)

print("File integrity check passed.")
