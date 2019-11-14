import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melbourne_file_path = 'varad.txt'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns

melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.label

melbourne_features = ['pr1', 'pr2', 'pr3', 'pr4', 'pr5', 'label']


X = melbourne_data[melbourne_features]


X.describe()
X.head()

melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
