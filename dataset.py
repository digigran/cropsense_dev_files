import pandas as pd
import numpy as np
def create_dataset():

    # Generating synthetic data for demonstration
    num_samples = 1000

    # Generating random values for features
    temperature = np.random.uniform(15, 35, num_samples)
    humidity = np.random.uniform(40, 90, num_samples)
    rainfall = np.random.uniform(50, 150, num_samples)
    soil_type = np.random.choice(['Sandy', 'Loamy', 'Clayey'], num_samples)
    region = np.random.choice(['North', 'South', 'East', 'West'], num_samples)

    # Generating random crop-growing practices
    irrigation = np.random.choice(['Drip', 'Sprinkler', 'Flood'], num_samples)
    fertilization = np.random.choice(['Organic', 'Inorganic'], num_samples)
    pest_control = np.random.choice(['Biological', 'Chemical'], num_samples)

    # Creating DataFrame
    data = pd.DataFrame({
        'Temperature': temperature,
        'Humidity': humidity,
        'Rainfall': rainfall,
        'Soil Type': soil_type,
        'Region': region,
        'Irrigation': irrigation,
        'Fertilization': fertilization,
        'Pest Control': pest_control
    })

    # Saving DataFrame to CSV file
    data.to_csv('crop_growing_practices.csv', index=False)
    print("Dataset creation complete.")
