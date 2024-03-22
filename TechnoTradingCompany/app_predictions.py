import pickle
import pandas as pd
import numpy as np
import os




with open('traffic_forecast_model', 'rb') as f:
    model_lgbm = pickle.load(f)


np.random.seed(0)
# Create a DataFrame with the desired structure
data = pd.DataFrame({
    'date': ['2023-08-01 18:00:00', '2023-08-01 18:00:00', '2023-08-01 18:00:00', '2023-08-02 11:00:00', '2023-08-02 11:00:00', '2023-08-02 11:00:00'],
    'temperature': [21, 21, 21, 19, 19, 19],
    'latitude': [45.045902, 45.072441, 45.220454, 45.045902, 45.072441, 45.220454],
    'longitude': [38.93860158420101, 39.000481, 37.596834, 38.93860158420101, 39.000481, 37.596834],
    'street': ['Краснодар, ул Северная, 70', 'Краснодар, ул. Московская улица 79/7', 'Краснодар, ул.Красная 127',
               'Краснодар, ул Северная, 70', 'Краснодар, ул. Московская улица 79/7', 'Краснодар, ул.Красная 127']
})


# Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Set the 'date' column as the index
data.set_index('date', inplace=True)

data['year'] = data.index.year
data['month'] = data.index.month
data['day'] = data.index.day
data['hour'] = data.index.hour
data['dayofweek'] = data.index.dayofweek

cat_columns=['year','month','day','hour','dayofweek','street']
for col in cat_columns:
    data[col]=data[col].astype('category')

# Drop the 'number_of_cars' column from the new data
features = data

# Make predictions using your trained model
predictions = model_lgbm.predict(features)

# Add the predictions to the data DataFrame
data['predictions'] = predictions

# Display the generated dataset
data.to_csv('predictions.csv')