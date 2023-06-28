import pandas as pd

# Function to read csv's
def read_csv(path: str):
    csv = pd.read_csv(    
        path,
        sep=";", 
        decimal=',' 
    )
    return csv

# Function to read special occupation datasets
def read_occ_data(main_path: str, year: int):
    occ_data = pd.read_csv(
        main_path + str(year) + '.csv', 
        sep=";", 
        decimal=','
    )
    return occ_data

# Function to clean and handle with occupation datasets
def clean_occ_dataset(occ_dataset):
    occ_dataset = occ_dataset[
    (occ_dataset['Data inicial'] != " ") 
    & 
    (occ_dataset['Hora inicial'] != " ") 
    & 
    (occ_dataset['Data final'] != " ") 
    & 
    (occ_dataset['Hora final'] != " ") 
    & 
    (occ_dataset['Total hores'] != " ")
    ]
    occ_dataset = occ_dataset.reset_index(drop=True)
    return occ_dataset

# Function to add the Covid feature to the dataset
def covid_column_creation(dataset):
    covid_range_1 = (
            (dataset['Date'] >= '2020-03-15') 
            & 
            (dataset['Date'] <= '2020-06-21')
        )
    covid_range_2 = (
            (dataset['Date'] >= '2020-10-25') 
            & 
            (dataset['Date'] <= '2021-05-09')
            )
    dataset.loc[covid_range_1 | covid_range_2, 'Covid'] = 1
    dataset['Covid'].fillna(0, inplace=True)

    return dataset

# Function to create the lagged features
def lagg_data(data, feature, lagged_feature_name, lags, days_loock_back, statistic):
    shift_t = days_loock_back*24
    shift_last = 7*24
    if statistic != 'last':
        for lag in lags:
            new_feture_name = lagged_feature_name + '_' + str(lag) + '_' + statistic
            if statistic == 'mean':
                data[new_feture_name] = (
                        data[feature]
                        .rolling(lag).mean()
                        .shift(shift_t)
                    )
            elif statistic == 'std':
                data[new_feture_name] = (
                        data[feature]
                        .rolling(lag).std()
                        .shift(shift_t)
                    )
            elif statistic == 'max':
                data[new_feture_name] = (
                        data[feature]
                        .rolling(lag).max()
                        .shift(shift_t)
                    )
            elif statistic == 'min':
                data[new_feture_name] = (
                        data[feature]
                        .rolling(lag).min()
                        .shift(shift_t)
                    )
    elif statistic == 'last':
        new_feture_name = lagged_feature_name + '_' + statistic
        data[new_feture_name] = (
                data[feature]
                .shift(shift_last)
            )
    return data
