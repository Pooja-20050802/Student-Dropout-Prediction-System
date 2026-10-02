import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# 1. Load dataset
DATA_FILE = r"C:\Users\pc638\Desktop\StudentDrop\Data\data.csv"

df = pd.read_csv(DATA_FILE, sep=";")

# Remove accidental spaces from column names
df.columns = df.columns.str.strip()

print("Dataset shape:", df.shape)
print("Target classes:")
print(df["Target"].value_counts())


# 2. Separate features and target
X = df.drop("Target", axis=1)
y = df["Target"]


# 3. Convert target labels to numbers
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

print("\nTarget mapping:")
for i, label in enumerate(label_encoder.classes_):
    print(i, "=", label)


# 4. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 5. Create Decision Tree model
model = DecisionTreeClassifier(
    random_state=42,
    max_depth=8
)


# 6. Train
print("\nTraining model...")
model.fit(X_train, y_train)

print("Training completed!")


# 7. Predict
y_pred = model.predict(X_test)


# 8. Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_encoder.classes_
    )
)


# 9. Save model + label encoder
joblib.dump(model, "dropout_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("\nModel saved as: dropout_model.pkl")
print("Label encoder saved as: label_encoder.pkl")