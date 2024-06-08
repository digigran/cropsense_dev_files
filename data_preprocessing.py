import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pickle

def preprocess_data():
    # Load the dataset
    data = pd.read_csv('crop_growing_practices.csv')

    # Separate features and target variable
    X = data.drop(columns=['Irrigation', 'Fertilization', 'Pest Control'])  # Features
    y = data[['Irrigation', 'Fertilization', 'Pest Control']]  # Target variables

    # Define preprocessing for numerical features
    numeric_features = ['Temperature', 'Humidity', 'Rainfall']
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())])

    # Define preprocessing for categorical features
    categorical_features = ['Soil Type', 'Region']
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    # Preprocess the data
    X_preprocessed = preprocessor.fit_transform(X)

    # Save preprocessor object to pickle file
    with open('preprocessor.pkl', 'wb') as f:
        pickle.dump(preprocessor, f)

    # Convert preprocessed data back to DataFrame
    X_preprocessed_df = pd.DataFrame(X_preprocessed, columns=numeric_features + \
                                    list(preprocessor.named_transformers_['cat'] \
                                        .named_steps['onehot'] \
                                        .get_feature_names_out(categorical_features)))

    # Save preprocessed data to CSV file
    preprocessed_data = pd.concat([X_preprocessed_df, y], axis=1)
    preprocessed_data.to_csv('preprocessed_crop_data.csv', index=False)
    print("Data preprocessing complete.")

preprocess_data()
