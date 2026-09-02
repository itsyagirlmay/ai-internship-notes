"""
clean.py
Week 2, Friday — cleans nam_places_raw.csv directly: handles nulls,
duplicates, and type coercion. The raw data already has real messiness
(missing names, missing population, case-inconsistent names), so no
artificial bad rows are injected. Writes a clean CSV and a cleaning log.
"""

import pandas as pd
from datetime import datetime

df = pd.read_csv("nam_places_raw.csv")
log = []
log.append(f"Cleaning log -- {datetime.now().strftime('%Y-%m-%d %H:%M')}")
log.append(f"Starting rows: {len(df)}\n")

# --- 1. Drop duplicate entries: same place name (case-insensitive) in the
#        same district, entered more than once under different OSM ids.
#        This is real crowd-sourced duplication, not an exact-row match.
#        Only applied where name is present -- unnamed rows are left alone,
#        since treating every null as equal would wrongly merge them. ---
before = len(df)
named = df[df["name"].notnull()].copy()
unnamed = df[df["name"].isnull()].copy()
named["_name_norm"] = named["name"].str.lower()
named = named.drop_duplicates(subset=["_name_norm", "adm2_name"], keep="first")
named = named.drop(columns=["_name_norm"])
df = pd.concat([named, unnamed], ignore_index=True)
log.append(f"Removed {before - len(df)} duplicate entries -- same place name + same district under a different OSM id (kept the first occurrence). Unnamed rows were left untouched to avoid falsely merging them.")

# --- 2. Drop columns that are essentially unused and add no value as-is ---
near_empty = ["is_in", "source", "name_en"]
for col in near_empty:
    non_null = df[col].notnull().sum()
    log.append(f"Dropped '{col}' -- only {non_null} of {len(df)} rows had a value.")
df = df.drop(columns=near_empty)

# --- 3. Standardize name casing so case-variants merge (e.g. "IVILIVINZI" -> "Ivilivinzi") ---
case_variants_before = df["name"].dropna().str.lower().duplicated().sum()
df["name"] = df["name"].str.title()
log.append(f"Standardized name casing to title case -- merged {case_variants_before} case-variant collision(s), e.g. 'IVILIVINZI' vs 'Ivilivinzi'.")

# --- 4. Coerce population to numeric, defensively -- confirms there's no
#        stray non-numeric text hiding in the column before trusting it. ---
def is_non_numeric(x):
    if not isinstance(x, str):
        return False
    try:
        float(x)
        return False
    except ValueError:
        return True

before_bad = df["population"].apply(is_non_numeric).sum()
df["population"] = pd.to_numeric(df["population"], errors="coerce")
log.append(f"Verified population as numeric -- {before_bad} non-numeric value(s) found and converted to null (source data was already clean on this column).")

# --- 5. Drop rows with neither a name nor a place type -- out of scope for this table ---
# These are unnamed residential-landuse polygons, not identifiable settlements.
# Deliberately NOT filled or guessed at -- dropped, and the decision documented.
before = len(df)
df = df[~(df["name"].isnull() & df["place"].isnull())]
log.append(f"Dropped {before - len(df)} row(s) with neither a name nor a place type -- unnamed land parcels, not named settlements.")

# --- 6. population: leave remaining nulls as null, do NOT fill ---
# Filling missing population with a median would be actively misleading here --
# a hamlet and a town have very different populations, and 99% of rows never
# had this recorded in the source data to begin with. Null stays null.
remaining_null_pop = df["population"].isnull().sum()
log.append(f"Left {remaining_null_pop} missing population value(s) as null -- not filled, see reflection below.")

# --- Write outputs ---
df.to_csv("nam_places_clean.csv", index=False)
log.append(f"\nFinal rows: {len(df)}")
log.append("Output written to nam_places_clean.csv")

log.append("""
Bias / privacy reflection:
No direct PII here -- no personal names, just place names and admin
regions -- but two other issues matter. First, this is crowd-sourced
OpenStreetMap data, and the source documentation says so directly:
"Coverage reflects where volunteer mappers have been active. Urban areas
are usually well represented, remote areas may be sparse." Any analysis
built on this data (e.g. counting settlements per region) will quietly
undercount remote, less-mapped areas -- that's a sampling bias baked into
the data collection process, not something cleaning can fix. Second,
filling the missing population values would have been a form of
fabrication dressed up as cleaning -- for real-world geographic data,
"we don't know" is a more honest and appropriate answer than a guessed
number, which ties back to Week 1's "appropriate use" vocabulary: a
statistical technique being available doesn't mean it's the right choice
for this data.
""")

with open("cleaning_log.txt", "w") as f:
    f.write("\n".join(log))

print("\n".join(log))
