import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# ==============================
# 1. Load dataset
# ==============================

FILE = r"C:\Users\pc638\Desktop\StudentDrop\Data\data.csv"

df = pd.read_csv(FILE, sep=";")

print("Original shape:", df.shape)

# ==============================
# 2. Remove unnecessary spaces
# ==============================

df.columns = df.columns.str.strip()

# ==============================
# 3. Check missing values
# ==============================

print("\nMissing values:")
print(df.isnull().sum().sum())

# ==============================
# 4. Separate features and target
# ==============================

X = df.drop("Target", axis=1)
y = df["Target"]

print("\nFeatures:", X.shape)
print("Target:", y.shape)

# ==============================
# 5. Encode target
# ==============================

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

print("\nTarget mapping:")

for label, number in zip(label_encoder.classes_, range(len(label_encoder.classes_))):
    print(label, "->", number)

# ==============================
# 6. Train-test split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# ==============================
# 7. Feature scaling
# ==============================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nScaling completed successfully.")

print("\nPreprocessing completed!")