# Script with all the needed features of each dataset we will use to build the new ones

hourly_electricity_needed_features = [
    'Date',
    'Hour'
]

classroom_occ_needed_features = [
    'Data inicial',
    'Hora inicial',
    'Hora final',
    'Espai'
]

classroom_info_needed_features = [
    'Ubicació',
    'Capacitat docència',
    'Superfície Centre Gestor',
    'Metres'
]

useful_features = [
    'Date', 
    'Hour', 
    'Capacitat docència', 
    'Superfície Centre Gestor', 'Metres'
]

features_lag = [
    'Total (General) [kWh] [C-Ciencies]',
    'I-Ciencies Comunicació (General) [kWh]',
    'Sabadell (General) [kWh]',
]

lag_features = {
    'Total (General) [kWh] [C-Ciencies]':  ['mean', 'std', 'min', 'max', 'last'],
    'I-Ciencies Comunicació (General) [kWh]': ['mean', 'std', 'min', 'max', 'last'],
    'Sabadell (General) [kWh]': ['mean', 'std', 'min', 'max', 'last'],
    'Superfície Centre Gestor': ['last'],
    'Metres': ['last'],
}



