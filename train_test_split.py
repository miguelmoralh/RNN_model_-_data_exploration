import pandas as pd
from datetime import datetime


def train_val_test_split(df, target_column):
    
    # Drop na values 
    df = df.dropna()
    
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year  
    
    # Define the periods for each split
    train_data = df[df['Year'].between(2018, 2020)]
    val_data = df[df['Year'] == 2021]
    test_data = df[df['Year'] == 2022] 
    
    # Drop some non needed columns
    columns_to_drop = ['Date', 'Hour', 'Datetime_hour', 'Year']
    train_data = train_data.drop(columns=columns_to_drop, axis=1)
    val_data = val_data.drop(columns=columns_to_drop, axis=1)
    test_data = test_data.drop(columns=columns_to_drop, axis=1)
    
    # Construct the dataframes
    X_train = train_data.drop(target_column, axis=1)
    y_train = train_data[[target_column]]
    X_val = val_data.drop(target_column, axis=1)
    y_val = val_data[[target_column]]
    X_test = test_data.drop(target_column, axis=1)
    y_test = test_data[[target_column]]
    return X_train, y_train, X_val, y_val, X_test, y_test
    

main_path = "C:/Users/Miguel/OneDrive/Escritorio/2n curs/2n Semestre/Synthesis Project I/Project/work_project/data/generated_datasets" 
science_bio_path = main_path + "/science_and_bio.csv"
communication_path = main_path + "/communication.csv"
sabadell_path = main_path + "/sabadell.csv"
science_and_bio_target = 'Total (General) [kWh] [C-Ciencies]'
communication_target = 'I-Ciencies Comunicació (General) [kWh]'
sabadell_target = 'Sabadell (General) [kWh]'
targets = [science_and_bio_target, communication_target, sabadell_target]
paths = [science_bio_path, communication_path, sabadell_path]




