import numpy as np
from sklearn.linear_model import Ridge
from joblib import dump
import os

# Example data: [average_runs, std_dev_runs] → actual next match runs
X = np.array([[50, 10], [30, 5], [70, 15], [10, 3], [90, 12]])
y = np.array([55, 35, 65, 12, 95])

model = Ridge()
model.fit(X, y)

# Save model
os.makedirs('models', exist_ok=True)
dump(model, 'models/performance_model.joblib')
