
import os
import pandas as pd

# Function to read CSV files
def read_csv(file_path):
    return pd.read_csv(file_path)

# Function to read JSON files
def read_json(file_path):
    return pd.read_json(file_path)

# Function to read Excel files
def read_excel(file_path):
    return pd.read_excel(file_path)

# Function to automatically detect and read files in a directory
def read_files_in_directory(directory_path):
    data_frames = {}
    for file in os.listdir(directory_path):
        if file.endswith('.csv'):
            df = read_csv(os.path.join(directory_path, file))
            data_frames[file] = df
        elif file.endswith('.json'):
            df = read_json(os.path.join(directory_path, file))
            data_frames[file] = df
        elif file.endswith('.xlsx'):
            df = read_excel(os.path.join(directory_path, file))
            data_frames[file] = df
    return data_frames

# Example usage of the function to read files in a directory
# Adjust the paths to the actual data directories
data_clients = read_files_in_directory('../../../OneDrive/Bureau/data/final/clients')
data_conseillers = read_files_in_directory('../../../OneDrive/Bureau/data/final/conseillers')
data_portfolios = read_files_in_directory('../../../OneDrive/Bureau/data/final/portfolios')
data_produits = read_files_in_directory('../../../OneDrive/Bureau/data/final/produits')
data_titres = read_files_in_directory('../../../OneDrive/Bureau/data/final/titres')

# This script is now ready with the correct paths for your PyCharm project.
