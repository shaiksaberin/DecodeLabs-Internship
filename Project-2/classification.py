from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# 1. Load the dataset
iris = load_iris()

X = iris.data
y = iris.target

print("====================================")
print("   Data Classification Using AI")
print("====================================")

print("\nDataset loaded successfully.")
print("Number of samples:", len(X))
print("Number of features:", X.shape[1])


# 2. Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# 3. Create and train the classification model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("\nModel trained successfully.")


# 4. Make predictions
y_pred = model.predict(X_test)


# 5. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel accuracy:", round(accuracy * 100, 2), "%")


# 6. Display some predictions
print("\nSample predictions:")

for i in range(5):
    actual = iris.target_names[y_test[i]]
    predicted = iris.target_names[y_pred[i]]

    print(
        "Actual:", actual,
        "| Predicted:", predicted
    )

print("\nClassification completed successfully.")