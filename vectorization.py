import pandas as pd
from sklearn.preprocessing import OneHotEncoder
def vectorize_data():

    # Load preprocessed data
    data = pd.read_csv('preprocessed_crop_data.csv')

    # Print column names for verification
    print("Column names:", data.columns)

    # Define categorical features for vectorization
    categorical_features = [col for col in data.columns if col.startswith('Soil Type_') or col.startswith('Region_')]

    # Apply one-hot encoding for categorical features
    encoder = OneHotEncoder(handle_unknown='ignore')
    X_encoded = encoder.fit_transform(data[categorical_features])

    # Convert encoded features to DataFrame
    X_encoded_df = pd.DataFrame(X_encoded.toarray(), columns=encoder.get_feature_names_out(categorical_features))

    # Drop original categorical features from the dataset
    data.drop(columns=categorical_features, inplace=True)

    # Concatenate encoded features with the remaining features
    X_vectorized = pd.concat([data, X_encoded_df], axis=1)

    # Save vectorized data to CSV file
    X_vectorized.to_csv('vectorized_crop_data.csv', index=False)
    print("Data vectorization complete.")
