import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


melbourne_file_path = 'varad.txt'
melbourne_data = pd.read_csv(melbourne_file_path) 

#melbourne_data = melbourne_data[0:1000]

print(melbourne_data.columns)


#melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.intId

melbourne_features = ['pr1', 'pr2', 'pr3', 'pr4', 'pr5']

melbourne_data = melbourne_data[2700:3000]


X = melbourne_data[melbourne_features]

print(X.describe())

print(X.head())



melbourne_model = RandomForestRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
#print(melbourne_model.predict(melbourne_data))
#print(melbourne_data[2600:2900])
