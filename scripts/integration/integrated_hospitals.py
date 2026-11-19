
import duckdb
from pathlib import Path

db = duckdb.connect()

db.sql("""
CREATE TABLE hospital AS
SELECT * FROM read_csv('data/csv/Hospital-General-Information-Cleaned.csv', all_varchar=true);

CREATE TABLE hcahps AS
SELECT * FROM read_csv('data/csv/HCAHPS-Survey-Cleaned.csv', all_varchar=true);

CREATE TABLE outcomes AS
SELECT * FROM read_csv('data/csv/Complications-Deaths-Cleaned.csv', all_varchar=true);
""")

db.sql("""
CREATE TABLE integrated AS

WITH survey AS (
    PIVOT hcahps
    ON "HCAHPS Measure ID"
    USING FIRST(TRY_CAST("HCAHPS Linear Mean Value" AS DOUBLE))
    GROUP BY "Facility ID"
),

clinical AS (
    PIVOT outcomes
    ON "Measure ID"
    USING FIRST(TRY_CAST("Score" AS DOUBLE))
    GROUP BY "Facility ID"
)

SELECT
    h.*,
    s.* EXCLUDE ("Facility ID"),
    c.* EXCLUDE ("Facility ID")

FROM hospital h

LEFT JOIN survey s
    ON h."Facility ID" = s."Facility ID"

LEFT JOIN clinical c
    ON h."Facility ID" = c."Facility ID"
""")

result = db.sql("""
SELECT
    COUNT(*) AS total,
    COUNT(DISTINCT "Facility ID") AS unique_hospitals
FROM integrated
""").fetchone()

assert result == (5419, 5419), "Integration validation failed"

Path("data/integrated").mkdir(parents=True, exist_ok=True)

db.sql("SELECT * FROM integrated").df().to_csv(
    "data/integrated/integrated_hospitals.csv",
    index=False
)

print("Integration successful!")
print("Total hospitals:", result[0])
print("Unique hospitals:", result[1])
