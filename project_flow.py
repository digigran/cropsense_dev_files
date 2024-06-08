import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from data_preprocessing import preprocess_data
from dataset import create_dataset
from vectorization import vectorize_data
from recommendation_logic import generate_recommendations

def run_project_flow():
    # Step 1: Data Preprocessing
    print("Step 1: Data Preprocessing...")
    preprocess_data()

    # Step 2: Dataset Creation
    print("Step 2: Dataset Creation...")
    create_dataset()

    # Step 3: Data Vectorization
    print("Step 3: Data Vectorization...")
    vectorize_data()

    # Step 4: Recommendation Logic
    print("Step 4: Recommendation Logic...")
    temperature = float(input("Enter temperature (in Celsius): "))
    humidity = float(input("Enter humidity (in percentage): "))
    rainfall = float(input("Enter rainfall (in mm): "))
    soil_type = input("Enter Soil Type: ")  # Add this line
    region = input("Enter Region: ")  # Add this line
    recommendations=generate_recommendations(temperature, humidity, rainfall, soil_type, region)  # Pass soil_type and region as arguments
    print("Recommendations:", recommendations)

    print("Project flow complete.")

if __name__ == "__main__":
    run_project_flow()