"""
explore_data.py
Week 2, Thursday — load a public CSV into pandas and inspect it before
touching it: shape, dtypes, null counts, and describe().

Dataset: nam_places_raw.csv — Namibia's Populated Places, flattened from
the HOTOSM (Humanitarian OpenStreetMap Team) GeoJSON export on HDX
(source: https://data.humdata.org/dataset/hotosm_nam_populated_places).
Properties only — geometry was dropped for this tabular exercise.
"""

import pandas as pd

df = pd.read_csv("nam_places_raw.csv")

print("=== Shape ===")
print(df.shape, "\n")

print("=== Dtypes ===")
print(df.dtypes, "\n")

print("=== Null counts per column ===")
print(df.isnull().sum(), "\n")

print("=== describe() ===")
print(df.describe(include="all"), "\n")

# --- What this data actually contains, and what looks wrong (3-4 sentences) ---
notes = """
Notes on nam_places_raw.csv:
This is 6,576 OpenStreetMap features across Namibia -- settlements
(villages, towns, cities) and residential land parcels, each tagged with
an id, name, place type, population, and administrative region. Two things
look wrong immediately: 5,050 rows (77%) have no name and 5,030 have no
place type -- mostly unnamed residential-landuse polygons rather than
actual named settlements, and population is missing in 6,536 of 6,576
rows (99%), which the dataset's own documentation explains as a coverage
gap, not bad data ("crowd sourced and cannot be considered exhaustive").
The is_in and source columns are essentially unused (2 and 0 non-null
values respectively) and add no value in their current form. There's also
at least one real duplicate-by-casing issue already visible in the raw
data: "Ivilivinzi" and "IVILIVINZI" refer to the same place.
"""
print(notes)
