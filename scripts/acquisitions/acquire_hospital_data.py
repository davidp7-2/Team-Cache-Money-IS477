import hashlib
from pathlib import Path

file_path = Path("data/raw/Hospital_General_Information.csv")

sha256_hash = hashlib.sha256()
with open(file_path, "rb") as file:
    for chunk in iter(lambda: file.read(4096), b""):
        sha256_hash.update(chunk)
        
checksum = sha256_hash.hexdigest()

print("Dataset:", file_path.name)
print("SHA256 Checksum:", checksum)
print("File Integrity check complete.")