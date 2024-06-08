import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import OneHotEncoder
from statistics import mode

def generate_recommendations(Temperature, Humidity, Rainfall, Soil_Type, Region):
    # Load preprocessed data
    data = pd.read_csv('vectorized_crop_data.csv')

    # Prepare user input data
    user_input = pd.DataFrame({
        'Temperature': [Temperature],
        'Humidity': [Humidity],
        'Rainfall': [Rainfall],
        'Soil Type_Clayey_0.0': [0],
        'Soil Type_Clayey_1.0': [0],
        'Soil Type_Loamy_0.0': [0],
        'Soil Type_Loamy_1.0': [0],
        'Soil Type_Sandy_0.0': [0],
        'Soil Type_Sandy_1.0': [0],
        'Region_East_0.0': [0],
        'Region_East_1.0': [0],
        'Region_North_0.0': [0],
        'Region_North_1.0': [0],
        'Region_South_0.0': [0],
        'Region_South_1.0': [0],
        'Region_West_0.0': [0],
        'Region_West_1.0': [0]
    })

    # Set one-hot encoded values based on Soil_Type
    if Soil_Type == 'Clayey':
        user_input['Soil Type_Clayey_0.0'] = 0
        user_input['Soil Type_Clayey_1.0'] = 1
    elif Soil_Type == 'Loamy':
        user_input['Soil Type_Loamy_0.0'] = 1
        user_input['Soil Type_Loamy_1.0'] = 0
    elif Soil_Type == 'Sandy':
        user_input['Soil Type_Sandy_0.0'] = 1
        user_input['Soil Type_Sandy_1.0'] = 0

    # Set one-hot encoded values based on Region
    if Region == 'East':
        user_input['Region_East_1.0'] = 1
    elif Region == 'North':
        user_input['Region_North_1.0'] = 1
    elif Region == 'South':
        user_input['Region_South_1.0'] = 1
    elif Region == 'West':
        user_input['Region_West_1.0'] = 1
 # Train a Nearest Neighbors model
    nn_model = NearestNeighbors(n_neighbors=5)
    nn_model.fit(data.drop(columns=['Fertilization', 'Pest Control', 'Irrigation']))  # Exclude target variables

    # Find nearest neighbors
    distances, indices = nn_model.kneighbors(user_input)

    # Get recommendations based on nearest neighbors
    recommendations_fertilization = data.iloc[indices[0]]['Fertilization']
    recommendations_pest_control = data.iloc[indices[0]]['Pest Control']
    recommendations_irrigation = data.iloc[indices[0]]['Irrigation']

    # Calculate mode for each category
    mode_fertilization = mode(recommendations_fertilization)
    mode_pest_control = mode(recommendations_pest_control)
    mode_irrigation = mode(recommendations_irrigation)

    # Print user-friendly recommendations
    print("Recommended fertilization method:", mode_fertilization)
    print("Recommended pest control method:", mode_pest_control)
    print("Recommended irrigation method:", mode_irrigation)

    return mode_fertilization, mode_pest_control, mode_irrigation