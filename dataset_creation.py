import pandas as pd
import numpy as np
import datetime

from utils.utils import read_csv, read_occ_data, clean_occ_dataset, covid_column_creation, lagg_data
from constant_variables import (
    hourly_electricity_needed_features,
    classroom_occ_needed_features,
    classroom_info_needed_features,
    useful_features,
    lag_features
)

main_path = "C:/Users/Miguel/OneDrive/Escritorio/2n curs/2n Semestre/Synthesis Project I/Project/work_project/data" 
ciencies_biociencies_path = main_path + "/ciencies_biociencies"
comunicacio_path = main_path + "/comunicacio"
sabadell_path = main_path + "/sabadell"
enginyeria_path = main_path + "/enginyeria"

### SCIENCE AND BIOSCIENCE FACULTY

# Read main data
classroom_info_ciencies_bio = read_csv(ciencies_biociencies_path + "/recursos_ciencies_biociencies.csv")
hourly_electricity_ciencies_bio = read_csv(ciencies_biociencies_path +  "/Consum_horari_electricitat_ciencies_biociencies_2018-2022.csv")

# Join the two consumption columns (trafo 1, trafo 2)
# Sum the two columns (type = float)
hourly_electricity_ciencies_bio['Total (General) [kWh] [C-Ciencies]'] = (
    hourly_electricity_ciencies_bio['C Ciències Trafo 1 (General) [kWh] [C-Ciencies]'] 
    + 
    hourly_electricity_ciencies_bio['C Ciències Trafo 2 (General) [kWh] [C-Ciencies]']
)

hourly_electricity_ciencies_bio = hourly_electricity_ciencies_bio.drop(
    [
    'C Ciències Trafo 1 (General) [kWh] [C-Ciencies]',
    'C Ciències Trafo 2 (General) [kWh] [C-Ciencies]'
    ], 
    axis=1
)

path_ciencies_occ_data = ciencies_biociencies_path + "/ocupacio_ciencies_biociencies_"
classroom_occupancy_ciencies_bio_2022 = read_occ_data(path_ciencies_occ_data, 2022)
classroom_occupancy_ciencies_bio_2021 = read_occ_data(path_ciencies_occ_data, 2021)
classroom_occupancy_ciencies_bio_2020 = read_occ_data(path_ciencies_occ_data, 2020)
classroom_occupancy_ciencies_bio_2019 = read_occ_data(path_ciencies_occ_data, 2019)
classroom_occupancy_ciencies_bio_2018 = read_occ_data(path_ciencies_occ_data, 2018)

occupation_ciencies_bio = pd.concat(
    [
        classroom_occupancy_ciencies_bio_2018, 
        classroom_occupancy_ciencies_bio_2019, 
        classroom_occupancy_ciencies_bio_2020, 
        classroom_occupancy_ciencies_bio_2021, 
        classroom_occupancy_ciencies_bio_2022
    ],
    ignore_index=True
)

# Remove non informative observations that provide us the same info as other observations.
occupation_ciencies_bio = clean_occ_dataset(occupation_ciencies_bio)

### COMMUNICATION FACULTY 

# Read main data
hourly_electricity_comunication = read_csv(comunicacio_path + "/Consum horari electricitat Comunicació 2018-2022.csv")
classroom_info_comunication = read_csv(comunicacio_path + "/recursos_ciencies_comunicacio.csv")
occupation_comunication = read_csv(comunicacio_path + "/ocupacio_ciencies_comunicacio_2018_2022.csv")
# Remove non informative observations that provide us the same info as other observations.
occupation_comunication = clean_occ_dataset(occupation_comunication)

### SABADELL FACULTY 

# Read main data
hourly_electricity_sabadell = read_csv(sabadell_path + "/Consum horari electricitat S 2018-2022.csv")
classroom_info_sabadell = read_csv(sabadell_path + "/recursos_escola_sabadell.csv")
occupation_sabadell = read_csv(sabadell_path + "/ocupacio_escola_sabadell_2018_2022.csv")

# Remove non informative observations that provide us the same info as other observations.
occupation_sabadell = clean_occ_dataset(occupation_sabadell)

### ENGINEERING FACULTY

classroom_info_engineering = read_csv(enginyeria_path + "/recursos_enginyeria.csv")
hourly_electricity_engineering = read_csv(enginyeria_path +  "/Consum horari electricitat Enginyeries 2018-2022.csv")

# Join the three consumption columns (trafo 1, trafo 2)
# Sum the three columns (type = float)
hourly_electricity_engineering['Total (General) [kWh] [Engineering]'] = (
    hourly_electricity_engineering['Q-Enginyeria (Cos Central) [kWh] [Q-Enginyeria]'] 
    + 
    hourly_electricity_engineering['Q-Enginyeria (Espina 4) [kWh] [Q-Enginyeria]']
    +
    hourly_electricity_engineering['Q-Enginyeria (Química) [kWh] [Q-Enginyeria]']   
)

hourly_electricity_engineering = hourly_electricity_engineering.drop(
    [
    'Q-Enginyeria (Cos Central) [kWh] [Q-Enginyeria]',
    'Q-Enginyeria (Espina 4) [kWh] [Q-Enginyeria]',
    'Q-Enginyeria (Química) [kWh] [Q-Enginyeria]'
    ], 
    axis=1
)

path_engineering_occ_data = enginyeria_path + "/ocupacio_enginyeria_"
classroom_occupancy_engineering_2022 = read_occ_data(path_engineering_occ_data, 2022)
classroom_occupancy_engineering_2021 = read_occ_data(path_engineering_occ_data, 2021)
classroom_occupancy_engineering_2020 = read_occ_data(path_engineering_occ_data, 2020)
classroom_occupancy_engineering_2019 = read_occ_data(path_engineering_occ_data, 2019)
classroom_occupancy_engineering_2018 = read_occ_data(path_engineering_occ_data, 2018)

occupation_engineering = pd.concat(
    [
        classroom_occupancy_engineering_2018, 
        classroom_occupancy_engineering_2019, 
        classroom_occupancy_engineering_2020, 
        classroom_occupancy_engineering_2021, 
        classroom_occupancy_engineering_2022
    ],
    ignore_index=True
)

# Remove non informative observations that provide us the same info as other observations.
occupation_engineering = clean_occ_dataset(occupation_engineering)

## BUT EGINEERIN FACULTY CANNOT BE ANALYSED AS ONE IMPORTANT FEATURE IS MISSING IN 
## THE INFO CLASSROOMS DATASET, THE 'CAPACITAT DOCENCIA'

### MERGING OPERATIONS 
hourly_electricity_datasets = [
    hourly_electricity_ciencies_bio, 
    hourly_electricity_comunication, 
    hourly_electricity_sabadell
]
classroom_info_datasets = [
    classroom_info_ciencies_bio, 
    classroom_info_comunication, 
    classroom_info_sabadell
]
occupation_datasets = [
    occupation_ciencies_bio,
    occupation_comunication,
    occupation_sabadell
]

# Merging the hourly electricity consumption dataset with the ocupation one
for index ,(hourly_electricity, occupation, class_info) in enumerate(zip(
    hourly_electricity_datasets,
    occupation_datasets,
    classroom_info_datasets
    )):
    occupation_by_hours = (
        hourly_electricity[hourly_electricity_needed_features]
        .merge(
            occupation[classroom_occ_needed_features],
            left_on='Date', 
            right_on='Data inicial',
            how='left'
        )
    )
    occupation_by_hours.dropna(inplace=True)
    
    # To ensure that the activity we are doing is done during the Hour 
    # in which we are measuring the hourly consumption electricity
    occupation_by_hours = (
        occupation_by_hours.loc[
            (occupation_by_hours['Hour'] >= occupation_by_hours['Hora inicial'])
            &
            (occupation_by_hours['Hour'] <= occupation_by_hours['Hora final']),
            :
        ]
    )
    
    # Merging with recursos dataset
    dataset_by_hours = (
        occupation_by_hours
        .merge(
            class_info[classroom_info_needed_features],
            left_on='Espai', 
            right_on='Ubicació',
            how='left'
            )
    )
    
    # Select only useful features
    dataset_by_hours = dataset_by_hours[useful_features]
    
    # Convert date column to datetime format
    dataset_by_hours['Date'] = pd.to_datetime(dataset_by_hours['Date'], format='%d/%m/%Y')
    occupation_by_hours_grouped = (
        dataset_by_hours
        .groupby(['Date', 'Hour'])
        .sum()
        .reset_index()
    )
    
    # Convert date column to datetime format
    hourly_electricity['Date'] = pd.to_datetime(hourly_electricity['Date'], format='%d/%m/%Y')
    
    # Compress the dataset in order to have a SINGLE observation for each date and hour
    hourly_spending_full= (
        hourly_electricity
        .merge(
            occupation_by_hours_grouped,
            on=['Date', 'Hour'],
            how='left'
        )
    )
    hourly_spending_full = hourly_spending_full.replace(np.nan, 0)
    
    # Create some time dependent features
    start_date = datetime.datetime(2018, 1, 1)  # initial date
    date_list = [start_date + datetime.timedelta(hours=x) for x in range(len(hourly_spending_full))]  
    hourly_spending_full['Datetime_hour'] = date_list
    hourly_spending_full["Weekday"] = hourly_spending_full["Datetime_hour"].dt.dayofweek +1
    hourly_spending_full["Month"] = hourly_spending_full["Datetime_hour"].dt.month 
    hourly_spending_full["Hour_2"] = hourly_spending_full["Datetime_hour"].dt.hour 
    
    # create a new column "Covid" and assign a value of 1 if the 'Date' is within the specified range
    hourly_spending_full = covid_column_creation(hourly_spending_full)
    
    
    # Adding lagged data
    lag_features_keys = list(lag_features.keys())
    lags_hours =  [24*7, 24*30]
    days_back = 2
    for element in hourly_spending_full.columns:
        for i, (feature_lag, statistics) in enumerate(lag_features.items()):
            if index == 0:
                if feature_lag == element:
                    for statistic in statistics:
                        lagged_feature_name = (
                            "lagged_" 
                            + feature_lag
                            .lower()
                            .replace(' ', '_')
                            .replace(',', '')
                            .replace('[', '')
                            .replace(']', '')
                        )
                        hourly_spending_full = lagg_data(
                            data=hourly_spending_full, 
                            feature=feature_lag,
                            lagged_feature_name=lagged_feature_name, 
                            lags=lags_hours,
                            days_loock_back=days_back,  
                            statistic=statistic
                                        )  
                    file_path = main_path + '/generated_datasets/science_and_bio.csv'
                    hourly_spending_full.to_csv(file_path,  sep = ';', decimal=',', index=False)
            if index == 1:
                if feature_lag == element:
                    for statistic in statistics:
                        lagged_feature_name = (
                            "lagged_" 
                            + feature_lag
                            .lower()
                            .replace(' ', '_')
                            .replace(',', '')
                            .replace('[', '')
                            .replace(']', '')
                        )
                        hourly_spending_full = lagg_data(
                            data=hourly_spending_full, 
                            feature=feature_lag,
                            lagged_feature_name=lagged_feature_name, 
                            lags=lags_hours,
                            days_loock_back=days_back,  
                            statistic=statistic
                        )
                    file_path = main_path + '/generated_datasets/communication.csv'
                    hourly_spending_full.to_csv(file_path,  sep = ';', decimal=',', index=False)
            if index == 2:
                if feature_lag == element:
                    lagged_feature_name = "Lagged conssumption"
                    for statistic in statistics:
                        lagged_feature_name = (
                            "lagged_" 
                            + feature_lag
                            .lower()
                            .replace(' ', '_')
                            .replace(',', '')
                            .replace('[', '')
                            .replace(']', '')
                        )
                        hourly_spending_full = lagg_data(
                            data=hourly_spending_full, 
                            feature=feature_lag,
                            lagged_feature_name=lagged_feature_name, 
                            lags=lags_hours,
                            days_loock_back=days_back,  
                            statistic=statistic
                        )
                    file_path = main_path + '/generated_datasets/sabadell.csv'
                    hourly_spending_full.to_csv(file_path, sep = ';', decimal=',', index=False)



