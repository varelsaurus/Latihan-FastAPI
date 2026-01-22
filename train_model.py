# Script to retrain the classifier model
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv('BankNote_Authentication.csv')

# Split features and target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Train model
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Check accuracy
y_pred = classifier.predict(X_test)
score = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {score:.4f}")

# Save model
with open("classifier.pkl", "wb") as f:
    pickle.dump(classifier, f)

print("Model saved to classifier.pkl")
