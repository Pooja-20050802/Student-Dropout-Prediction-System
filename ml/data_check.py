import pandas as pd

# Change this to your actual CSV filename
FILE = r"C:\Users\pc638\Desktop\StudentDrop\Data\data.csv"

# Load UCI dataset
df = pd.read_csv(FILE, sep=";")

print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)
print(df.shape)

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")

print("\n" + "=" * 60)
print("TARGET DISTRIBUTION")
print("=" * 60)
print(df["Target"].value_counts())

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)
print(df.isnull().sum().sum())

print("\n" + "=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)
print(df.head())