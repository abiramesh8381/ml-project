import pandas as pd
import numpy as np

# -------------------------------
# Load Data
# -------------------------------
data = {
    'patient_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 101, 107, 118, 119, 120],
    'age': ['25', '34', None, '45', '29', None, '38', '52', '27', '41',
            '33', 'unknown', '48', '26', '35', '25', '38', '31', None, '44'],
    'weight': ['70', '65', '80', None, '75', None, '68', '90', '72', '85',
               '78', None, '82', '69', 'N/A', '70', '68', '74', None, '88'],
    'blood_pressure': [120, 130, None, 140, 125, None, 135, None, 118, 145,
                      128, None, 138, 122, None, 120, 135, 126, None, 142],
    'medication': ['Aspirin', 'Metformin', 'Lisinopril', None, 'Aspirin',
                   'Metformin', 'Lisinopril', 'Aspirin', None, 'Metformin',
                   'Lisinopril', 'Aspirin', None, 'Metformin', 'Aspirin',
                   'Aspirin', 'Lisinopril', 'Metformin', 'Aspirin', None],
    'insurance_provider': ['Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None,
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', 'Blue Cross',
                          'Aetna', None, 'UnitedHealth', 'Blue Cross', 'Aetna',
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None]
}

df = pd.DataFrame(data)

# -------------------------------
# Task 1: Inspect the Data
# -------------------------------
print("=== Initial Inspection ===")
print(df.info())
print("Missing values per column:\n", df.isnull().sum())
print("Percentage missing:\n", (df.isnull().sum() / len(df)) * 100)
print("Duplicate rows:", df.duplicated().sum())

# -------------------------------
# Task 2: Data Type Conversion
# -------------------------------
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['weight'] = pd.to_numeric(df['weight'], errors='coerce')

# Fill insurance_provider first, then convert to category
df['insurance_provider'] = df['insurance_provider'].fillna('Unknown')
df['insurance_provider'] = df['insurance_provider'].astype('category')

print("\n=== After Type Conversion ===")
print(df.dtypes)
print("Missing values after conversion:\n", df.isnull().sum())

# -------------------------------
# Task 3: Handle Missing Values
# -------------------------------
df['age'] = df['age'].fillna(df['age'].median())
df['weight'] = df['weight'].fillna(df['weight'].median())
df['blood_pressure'] = df['blood_pressure'].fillna(df['blood_pressure'].median())
df['medication'] = df['medication'].fillna(df['medication'].mode()[0])

print("\n=== After Handling Missing Values ===")
print(df.isnull().sum())

# -------------------------------
# Task 4: Handle Duplicates
# -------------------------------
print("\nDuplicate rows (full):")
print(df[df.duplicated(keep=False)])

print("\nDuplicate patient_id flags:")
print(df.duplicated(subset=['patient_id']))

print("Shape before:", df.shape)
df = df.drop_duplicates(subset=['patient_id'], keep='first')
print("Shape after:", df.shape)

# -------------------------------
# Task 5: Verification Report
# -------------------------------
print("\n=== Verification Report ===")
print("Final Shape:", df.shape)
print("Final Missing Values:\n", df.isnull().sum())
print("Final Duplicates:", df.duplicated(subset=['patient_id']).sum())
print("Final Data Types:\n", df.dtypes)

print("\n=== Cleaned Data (first 5 rows) ===")
print(df.head())
