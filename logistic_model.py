# 1. Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 2. Load Data
df = pd.read_csv('data/orders_returns.csv')

# 3. Select Features
features = ['category', 'supplier', 'customer_location', 'marketing_channel',
            'price', 'quantity', 'delivery_time']
target = 'return_status'
X = df[features]
y = df[target]

# 4. Preprocessing Pipeline
categorical_cols = ['category', 'supplier', 'customer_location', 'marketing_channel']
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(drop='first'), categorical_cols)],
    remainder='passthrough'
)

# 5. Model Pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000, class_weight='balanced'))
])

# 6. Train-Test Split & Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# 7. Evaluation
y_pred = model.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# 8. Predict Return Probabilities
df['return_probability'] = model.predict_proba(X)[:, 1]

# 9. Save High-Risk Products
high_risk = df[df['return_probability'] >= 0.5]
high_risk.to_csv('results/high_risk_products.csv', index=False)
print("High-risk products saved to results/high_risk_products.csv")

