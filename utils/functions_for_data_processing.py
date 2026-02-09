import numpy as np
import pandas as pd


def mixed_dtypes_detector(df):
    mixed_dtypes = {}
    for column in df.columns:
        types = df[column].apply(lambda x: type(x).__name__).value_counts()
        if len(types) > 1:
            mixed_dtypes[column] = types.to_dict()
            
    return mixed_dtypes

def missing_values_info(df):
    missing_values = df.isnull().sum()
    missing_values_percentage = round(((missing_values / len(df)) * 100), 3)
    missing_values_table = pd.concat(
        [missing_values, missing_values_percentage],
        keys=['Missing Count', 'Missing Percentage'],
        axis=1
    )
    
    return missing_values_table

def suspicious_values_detector(df, suspicious_values, inplace_replace=False):
    results = []
    for column in df.columns:
        value_counts = df[column].value_counts()
        for value in suspicious_values:
            if value in value_counts.index:
                count = value_counts.loc[value]
                results.append(
                    f'Column {column} contains {count} instances of {value}.'
                )
    if inplace_replace == True:
        for column in df.columns:
            for suspicious_value in suspicious_values:
                df[column] = df[column].where(df[column] != suspicious_value, np.nan)
        return df
    
    return results
